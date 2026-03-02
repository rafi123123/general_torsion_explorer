# Knot Group Representations: Wirtinger vs. Triangulation

When working with the fundamental group of a knot complement , there are two primary ways to describe the group. While they look different algebraically, they are **isomorphic**, meaning they describe the exact same mathematical object.

## 1. Wirtinger Representation (Diagram-Based)

The **Wirtinger presentation** is the "classic" method derived directly from a 2D knot diagram.

* **Generators:** Each over-crossing arc in the knot diagram is assigned a generator (representing a loop around that strand).
* **Relators:** Each crossing point in the diagram produces a relation of the form .
* **Intuition:** It is highly visual and directly tied to the physical geometry of the knot's strands.

## 2. Triangulation Representation (SnapPy/Manifold-Based)

**SnapPy** and similar software view the knot complement as a 3D manifold.

* **Generators:** These are derived from the edges of **ideal tetrahedra** that are glued together to fill the space around the knot.
* **Relators:** These describe how the faces of those tetrahedra are identified (glued) to form a complete manifold.
* **Optimization:** SnapPy uses simplification algorithms (like Tietze transformations) to provide the shortest possible "word" for the relators. This is why a SnapPy relator like `abbbaBAAB` is often much shorter than a Wirtinger string.

---

## 3. Validity Across Representations

**Crucial Note for Algorithms:**
Because these two representations describe the same group, any property found in one—specifically **generalized torsion**—is valid for the other.

If you find a word  that is a generalized torsion element in the SnapPy representation, there exists an equivalent word in the Wirtinger representation. The choice of representation is a matter of **computational efficiency**, not mathematical correctness. Your generalized torsion results are properties of the *knot group itself*, not the specific alphabet used to write it.

---

## 4. Knot Naming Conventions

When searching for knots in different databases, you will encounter different naming systems:

* **Alexander-Briggs Notation (e.g., , ):** The classic system based on crossing number and an arbitrary index.
* [KnotInfo Database](https://www.google.com/search?q=https://knotinfo.math.indiana.edu/)


* **Dowker-Thistlethwaite (DT) Code:** A numerical sequence representing the crossings, used heavily in computer-aided knot theory.
* [Understanding DT Codes](https://en.wikipedia.org/wiki/Dowker%E2%80%93Thistlethwaite_notation)


* **Conway Notation:** Describes knots based on their "tangle" structure.
* [Conway Notation Overview](https://www.google.com/search?q=https://mathworld.wolfram.com/ConwayNotation.html)



---

## Further Reading & Resources

### Mathematical Theory

* [Knots and Links (Dale Rolfsen)](https://www.google.com/search?q=https://books.google.com/books/about/Knots_and_Links.html%3Fid%3DfW_fAAAAMAAJ) – The definitive text on Wirtinger presentations and knot groups.
* [The Geometry and Topology of Three-Manifolds (Thurston)](https://www.google.com/search?q=http://library.msri.org/books/gt3m/) – Explains the triangulation and hyperbolic structures used by SnapPy.

### Computational Tools

* [SnapPy Documentation: Fundamental Groups](https://www.google.com/search?q=https://snappy.computop.org/fundamental_group.html) – How SnapPy handles group presentations and simplifications.
* [KnotPlot](http://www.knotplot.com/) – For visualizing the 2D arcs associated with Wirtinger generators.
* [Generalized Torsion in Knot Groups (Naylor/Rolfsen)](https://arxiv.org/abs/1404.1423) – A paper exploring torsion in these specific group contexts.

---

**Would you like me to add a section specifically explaining how to convert between these two representations using Tietze transformations?**