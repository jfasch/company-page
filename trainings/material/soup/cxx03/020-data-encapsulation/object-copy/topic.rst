.. include:: <mmlalias.txt>

.. jf-topic:: cxx03.data_encapsulation.object_copy
   :dependencies: cxx03.data_encapsulation.ctor_dtor


Object Copy
===========

Copy in C
---------

**Copy of objects in C**: ``struct``

.. list-table::

   * * .. code-block:: c++

          struct point
          {
              int x;
              int y;
          };

     * .. code-block:: c++

          struct point p1 = {2,7};
	  struct point p2;

	  p2 = p1;

* ``struct point``: *memberwise* copy
* Simple: transfer of memory image

Copy Constructor
----------------

**Copying objects in C**: similar to C++

.. list-table::

   * * .. code-block:: c++

          class point
          {
              // ...
          };
          ...
          point p1;
          point p2(p1);

     * * Compiler *generates copy constructor*
       * |longrightarrow| member by member
       * |longrightarrow| simple data types just as in C

**But ...**

Copy Constructor and Pointer Members (1)
----------------------------------------

**Caution, Trap**: pointer members

.. list-table::

   * * .. code-block:: c++

          class String
          {
          public:
              String(const char *c_str);
          private:
              char *_c_str;
          };

       .. code-block:: c++

          String s1("hello");
          String s2 = s1; // ctor!

     * 

       .. image:: 02-02-00-pointer-member.dia

Copy Constructor and Pointer Members (2)
----------------------------------------

**Segmentation Fault** in the best of all cases ...

.. list-table::

   * * * Pointer member is to compiler simply *a pointer*
       * Pointers are copied
       * But not what they point to
       * The first of both objects that is destroyed frees memory
       * *How should the compiler know!*

     * 
     
       .. image:: 02-02-00-pointer-member-segfault.dia

Copy Constructor and Pointer Members (3)
----------------------------------------

**Solution**

* Explicit copy constructor
* Copy the memory pointed to

.. list-table::

   * * .. code-block:: c++

          String::String(const String& s)
          {
              _c_str = new char[
                   strlen(s._c_str)+1];
              strcpy(_c_str, s._c_str);
          }

     * 

       .. image:: 02-02-00-pointer-member-2.dia

Copy Constructor: Recursive/Memberwise
--------------------------------------

.. list-table::

   * * .. code-block:: c++

          struct TwoStrings
          {
              String s1;
              String s2;
          };
          struct TwoTwoStrings
          {
              TwoStrings s21;
              TwoStrings s22;
          };

     * * ``String`` has copy constructor (correct because handwritten)
       * |implies| ``TwoStrings`` is correct
       * |implies| ``TwoTwoStrings`` is correct
       * |implies| ...

Assignment Operator
-------------------

**Second way of copying objects:** overwrite an existing object

.. list-table::

   * * .. code-block:: c++

          class point
          {
              // ...
          };

	  point p1, p2;
	  // ...
	  p2 = p1; // assignment!

     * * Like *Copy Constructor* generated by compiler
       * |longrightarrow| Member by member
       * |longrightarrow| simple data types just as in C

**But ...** 

* As with the copy constructor |longrightarrow| pointer members!
* Assignment operator is best self defined when pointer members are
  involved

Assignment Operator and Pointer Members: Memory Leak
----------------------------------------------------

**Caution, naively buggy!**

.. list-table::

   * * .. code-block:: c++

          String& String::operator=(
              const String& s)
          {
              _c_str = new char[
                  strlen(s._c_str)+1];
              strcpy(_c_str, s._c_str);
              return *this;
          }

	  String s1("hello");
	  String s2("hallo");
	  s2 = s1;     // LEAK!

     * 

       .. image:: 02-02-00-pointer-member-assignment-operator.dia

Assignment Operator and Pointer Members: Memory Leak, Straighforward Fix
------------------------------------------------------------------------

**Caution, still naively buggy!**

.. code-block:: c++

   String& String::operator=(
       const String& s)
   {
       delete[] _c_str;        // BUG!!
       _c_str = new char[
           strlen(s._c_str)+1];
       strcpy(_c_str, s._c_str);
       return *this;
   }

**WTF, why could this be a bug??**

Assignment Operator and Pointer Members: *Self-Assignment*
----------------------------------------------------------

Correct nonsense ...

* Why would somebody want to write this?
* But anyway, it is legal!

.. list-table::

   * * .. code-block:: c++

          int i = 42;
          i = i;

     * .. code-block:: c++

          String s("hello");
	  s = s;      // SEGFAULT!! (if you're lucky)

* *Self Assignment*
* Rare but true!
* User expects that this is not an error

Assignment Operator: *Self Assignment*, Correctly Implemented
-------------------------------------------------------------

**Ultimate Fix**: *Self Assignment Check*

.. code-block:: c++

   String& String::operator=(
       const String& s)
   {
       if (this != &s)} {        // SELF ASSIGNMENT CHECK!!
           delete[] _c_str;
           _c_str = new char[
               strlen(s._c_str)+1];
           strcpy(_c_str, s._c_str);
       }
       return *this;
   }
