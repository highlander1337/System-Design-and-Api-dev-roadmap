/**
 * Unit tests for Demo class using JUnit 4.
 */

import static org.junit.Assert.*;
import org.junit.Test;

import java.io.InputStream;
import java.io.PrintStream;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;

public class DemoTest {

    // ---------------------------------------------------------
    // Unit tests for isTriangle()
    // ---------------------------------------------------------

    @Test 
    public void testIsTriangle_ValidTriangles() {

        assertTrue(Demo.isTriangle(3, 4, 5));

        assertTrue(Demo.isTriangle(5, 5, 5));

        assertTrue(Demo.isTriangle(2, 3, 4));

        assertTrue(Demo.isTriangle(1, 2, 2));

        assertTrue(Demo.isTriangle(2, 1, 2));

    }


    @Test 
    public void testIsTriangle_InvalidTriangles() {

        assertFalse(Demo.isTriangle(1, 2, 3));

        assertFalse(Demo.isTriangle(2, 3, 5));

        assertFalse(Demo.isTriangle(0, 1, 1));

        assertFalse(Demo.isTriangle(1, 0, 1));

        assertFalse(Demo.isTriangle(1, 1, 0));

        assertFalse(Demo.isTriangle(-1, 2, 2));

        assertFalse(Demo.isTriangle(2, -1, 2));

        assertFalse(Demo.isTriangle(2, 2, -1));

        assertFalse(Demo.isTriangle(10, 1, 1));

        assertFalse(Demo.isTriangle(1, 10, 1));

        assertFalse(Demo.isTriangle(1, 1, 10));

    }


    @Test 
    public void testIsTriangle_EdgeCases() {

        assertTrue(Demo.isTriangle(1, 1, 1));

        assertTrue(Demo.isTriangle(2, 3, 4));

        assertTrue(Demo.isTriangle(4, 3, 2));

        assertTrue(Demo.isTriangle(3, 4, 2));

        assertTrue(Demo.isTriangle(1000, 1001, 1002));

    }


    @Test public void testIsTriangle_Mutations() {

        assertFalse(Demo.isTriangle(1, 2, 4));

        assertFalse(Demo.isTriangle(2, 2, 5));

        assertFalse(Demo.isTriangle(3, 1, 5));

    }

    // ---------------------------------------------------------
    // Integration tests for main()
    // ---------------------------------------------------------

    @Test(timeout = 2000)
    public void testMain_ValidTriangleInput() throws Exception {
        String input = "3\n4\n5\n";
        String expected = "This is a triangle.";
        String output = runMainWithInput(input);
        assertTrue(output.contains(expected));
    }

    @Test(timeout = 2000)
    public void testMain_InvalidTriangleInput() throws Exception {
        String input = "1\n2\n3\n";
        String expected = "This is not a triangle.";
        String output = runMainWithInput(input);
        assertTrue(output.contains(expected));
    }

    @Test(timeout = 2000)
    public void testMain_ZeroLengthInput() throws Exception {
        String input = "0\n4\n5\n";
        String expected = "This is not a triangle.";
        String output = runMainWithInput(input);
        assertTrue(output.contains(expected));
    }

    @Test(timeout = 2000)
    public void testMain_NegativeLengthInput() throws Exception {
        String input = "-1\n4\n5\n";
        String expected = "This is not a triangle.";
        String output = runMainWithInput(input);
        assertTrue(output.contains(expected));
    }

    @Test(timeout = 2000)
    public void testMain_BoundaryEquality() throws Exception {
        String input = "2\n3\n5\n";
        String expected = "This is not a triangle.";
        String output = runMainWithInput(input);
        assertTrue(output.contains(expected));
    }

    // Smoke tests
    @Test(timeout = 2000)
    public void testMain_MethodExecution() throws Exception {
        String input = "3\n4\n5\n";
        String output = runMainWithInput(input);
        assertTrue(output.contains("This is a triangle."));
    }

    @Test(timeout = 2000)
    public void testMain_MethodExecutionWithArgs() throws Exception {
        String input = "3\n4\n5\n";
        String output = runMainWithInput(input, new String[]{"3", "4", "5"});
        assertTrue(output.contains("This is a triangle."));
    }

    // ---------------------------------------------------------
    // Utility method
    // ---------------------------------------------------------

    private String runMainWithInput(String input) throws Exception {
        return runMainWithInput(input, new String[]{});
    }

    private String runMainWithInput(String input, String[] args) throws Exception {
        InputStream originalIn = System.in;
        PrintStream originalOut = System.out;
        ByteArrayInputStream in = new ByteArrayInputStream(input.getBytes());
        ByteArrayOutputStream out = new ByteArrayOutputStream();

        System.setIn(in);
        System.setOut(new PrintStream(out));

        try {
            Demo.main(args);
        } finally {
            System.setIn(originalIn);
            System.setOut(originalOut);
        }

        return out.toString();
    }
}
