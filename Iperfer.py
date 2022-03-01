import edu.pace.cs242.Metrics;
import edu.pace.cs242.StackException;

import java.io.PrintWriter;

import static edu.pace.cs242.DatasetP.datasetP;

/**
 * A class to verify balanced parentheses strings.
 */
public class BalancedParentheses
{
  static String metPushes = "stack pushes";
  static String metPops = "stack pops";
  Metrics metrics;
  StackNode stackTop;
/**
 * Construct a class instance and initialize the Metrics counters.
 * @param mtr a Metrics object
 */
BalancedParentheses(Metrics mtr) {
  if (null == mtr)
  {
    metrics = new Metrics();
  }
  else
  {
    metrics = mtr;
    metrics.addCounter(metPushes);
    metrics.addCounter(metPops);
  }
}
/**
 * Push the passed data item onto the stack, making iot the new top.
 * @param dat the data item to be pushed on the stack
 */
void push(char dat)
{
    stackTop = new BalancedParentheses.StackNode(dat, stackTop);
}
/**
 * Pop the top data item off the stack and return it.
 * @return the top data item
 * @throws StackException if the stack is empty
 */
char pop() throws StackException
{
  StackNode nod;
  if (stackTop == null){throw new StackException("empty stack");}
  nod = stackTop;
  stackTop = nod.link;
  return nod.data;
}
/**
 * Return the top data item in the stack without popping.
 * @return the stack top
 * @throws StackException if the stack is empty
 */
char top() throws StackException
{
  /*We return stackTop, and if stackTop is null then we throw the exception as indicated*/
  if (stackTop == null) { throw new StackException("empty stack");}
  return stackTop.data;
}
/**
 * Verifies the passed String is a sequence of balanced parentheses.
 * @param data the ijnput sequence of parentheses
 * @return true if the input is balanced, false otherwise
 * @throws StackException on a problem
 */
boolean balanced(String data)
    throws StackException
{
  char ch;
  
  for (int i = 0; i < data.length(); ++i){
    ch = data.charAt(i);
    if (ch == '(')
    {
      push(ch);
      metrics.count(metPushes);
    }
    else if (ch == ')'){
      metrics.count(metPops);
      if (pop() != '('){
        throw new StackException("unpaired parentheses");
      }
      else{
        throw new StackException("Invalid input: " + ch);
      }
    }
  }
  return null == stackTop;
}
public static void main(String[] args)
{
  BalancedParentheses blp;
  Metrics metrics = new Metrics();
  PrintWriter pw = new PrintWriter(System.out);
  int ix;
  String[] datas;
  String[] testData = {"(())()", "()()()", "(((())))(())()",
      "(()(())((()(())((()))))"};
  datas = datasetP;
//  datas = testData;
  blp = new BalancedParentheses(metrics);
  for (ix = 0; ix < datas.length; ++ix)
  {
    metrics.reset();
    try
    {
      if (blp.balanced(datas[ix]))
        pw.printf("record %d: balance check succeeded\n", ix);
      else
        pw.printf("record %d: balance check failed\n", ix);
    }
    catch (StackException stx)
    {
      pw.printf("record %d: %s\n", ix, stx.getMessage());
    }
    metrics.display(pw);
  }
  pw.close();
}
/**
 * A StackNode for a linked-list stack implementation.
 */
class StackNode
{
  private final StackNode link;
  private final char data;
  private StackNode(char dat, StackNode lnk)
  {
    data = dat;
    link = lnk;
  }
}
}
