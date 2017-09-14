#ifndef EXAMPLE_H
#define EXAMPLE_H

// COPYRIGHTNOTICE

/**
 * @file
 * @author AUTHOR
 * @version 1.0
 *
 * @section DESCRIPTION
 *
 * An example class for the HSF
 *
 *
 */

namespace PROJECTTEMPLATE {

  class Example {
  public:
    /// Default constructor
    Example();

    /// Default destructor
    virtual ~Example();

    /**
     * Constructor from a given number
     *
     * @param number initial value
     */
    Example(int number);

    /**
     * Get current value
     */
    int get() const;

    /**
     * Set new value
     *
     * @param number new value
     *
     */
     void set(int number);

  private:
    /// Internally stored number
    int m_number;
  };
}

#endif
