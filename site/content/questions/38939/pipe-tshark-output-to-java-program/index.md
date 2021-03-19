+++
type = "question"
title = "pipe tshark output to java program"
description = '''i want to pipe packets from tshark to java program  when i use this command  tshark -i 1 -T fields -e frame.number -e ip.src -e tcp.window_size_value -e frame.time -e data.text -e tcp.analysis.duplicate_ack -e tcp.analysis.out_of_order -e tcp.analysis.retransmission -e tcp.analysis.fast_retransmissi...'''
date = "2015-01-08T02:34:00Z"
lastmod = "2015-01-08T05:32:00Z"
weight = 38939
keywords = [ "tshark" ]
aliases = [ "/questions/38939" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pipe tshark output to java program](/questions/38939/pipe-tshark-output-to-java-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38939-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to pipe packets from tshark to java program</p><p>when i use this command<br />
</p><pre><code>tshark -i 1 -T fields -e frame.number -e ip.src -e tcp.window_size_value -e frame.time -e data.text -e tcp.analysis.duplicate_ack -e tcp.analysis.out_of_order -e tcp.analysis.retransmission -e tcp.analysis.fast_retransmission -e tcp.analysis.spurious_retransmission -e tcp.analysis.zero_window -e tcp.stream -E header=y -E separator=, &gt;output.csv</code></pre><p>it create output.csv file with columns i mentioned in the command</p><p>i want to flush packets captured by tshark to java program so i found this code</p><pre><code>package javaapplication25;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.*;

/**
 *
 * @author shedalap
 */
public class JavaApplication25 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)throws IOException{

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String s;
        while ((s=in.readLine())!=null&amp;&amp;s.length()!=0) {
            System.out.println(in.read());
        }
    }
}</code></pre><p>when i run the program no problems</p><p>in tshark i put this command</p><pre><code>tshark -r 111.pcapng -T fields -e frame.number -e ip.src -e tcp.window_size_value -e frame.time -e data.text -e tcp.analysis.duplicate_ack -e tcp.analysis.out_of_order -e tcp.analysis.retransmission -e tcp.analysis.fast_retransmission -e tcp.analysis.spurious_retransmission -e tcp.analysis.zero_window -e tcp.stream -E header=y -E separator=, -l | java &quot;C:\Users\shedalap\Documents\NetBeansProjects\JavaApplication25\build\classes\javaapplication25.class&quot;</code></pre><p>i get this error</p><p>tshark : an error occurred while printing packets : invalid arguments</p><p>why what is wrong ?</p><p>thank you very much</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '15, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/583f60448e616e6c6f8408eb6620006a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shady&#39;s gravatar image" /><p>shady<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shady has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '15, 02:55</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-38939" class="comments-container"><span id="38940"></span><div id="comment-38940" class="comment"><div id="post-38940-score" class="comment-score"></div><div class="comment-text"><p>i think i am close when i entered this command</p><p>tshark -i 1 -f -T fields -f -e frame.number -f -e ip.src -e tcp.win dow_size_value -e frame.time -e data.text -e tcp.analysis.duplicate_ack -e tcp.a nalysis.out_of_order -e tcp.analysis.retransmission -e tcp.analysis.fast_retrans mission -e tcp.analysis.spurious_retransmission -e tcp.analysis.zero_window -e t cp.stream -E header=y -E separator=, -l &gt; java "C:\Users\shedalap\Documents\NetB eansProjects\JavaApplication25\build\classes\javaapplication25.class"</p><p>this should be capture filter but there is syntax error what is it ??</p></div><div id="comment-38940-info" class="comment-info"><span class="comment-age">(08 Jan '15, 02:57)</span> shady</div></div><span id="38945"></span><div id="comment-38945" class="comment"><div id="post-38945-score" class="comment-score"></div><div class="comment-text"><blockquote><p>'&gt; java ...'</p></blockquote><p>This will write a file named 'java' in the directory where you started tshark, with the output of thshark! It will NOT run <strong>java</strong>!</p></div><div id="comment-38945-info" class="comment-info"><span class="comment-age">(08 Jan '15, 04:45)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-38939" class="comment-tools"></div><div class="clear"></div><div id="comment-38939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38950"></span>

<div id="answer-container-38950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38950-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tshark : an error occurred while printing packets : invalid arguments</p></blockquote><p>That's because nothing is reading what tshark writes to STDOUT, probably because your Java program does not work as you expect it.</p><p>You'll get the same tshark error, if you pipe thshark output to <strong>dir</strong> (not reading from STDIN).</p><p>So, please check the error message you get when you run the following command:</p><blockquote><p>echo "huhu" | java "C:\Users\shedalap\Documents\NetB eansProjects\JavaApplication25\build\classes\javaapplication25.class"</p></blockquote><p>And then ask your local Java guru what that means and how to fix it.</p><p><strong>++ UPDATE ++</strong></p><p>I did not see the <strong>package</strong> statement in the Java code in the first place. This, and the way you are running the Java code (with .class) causes the termination of your java process with errors.</p><p>So, to fix your Java problem, <strong>still ask your local Java guru</strong>, as this ia the Wireshark Q&amp;A site!</p><p>Besides that you can try to either remove the <strong>package</strong> statement or call your Java code in a different way.</p><p><strong>Without</strong> <code>package</code> statement:<br />
</p><blockquote><p>java JavaApplication25 (no .class !!!)</p></blockquote><p><strong>With</strong> <code>package</code> statement:<br />
</p><blockquote><p>mkdir JavaApplication25<br />
copy JavaApplication25.class to JavaApplication25<br />
run: java JavaApplication25.JavaApplication25</p></blockquote><p>See the following discussion (and google) for an explanation: <a href="http://stackoverflow.com/questions/3081689/why-cant-i-run-my-java-hello-world-program-if-it-is-inside-a-package">http://stackoverflow.com/questions/3081689/why-cant-i-run-my-java-hello-world-program-if-it-is-inside-a-package</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '15, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '15, 07:10</p></div></div><div id="comments-container-38950" class="comments-container"><span id="38991"></span><div id="comment-38991" class="comment"><div id="post-38991-score" class="comment-score"></div><div class="comment-text"><p>thank you very much</p><p>removing package statement helped me very much it worked now tshark capture packets and flushes them to javaapplication25 by using this command in tshark</p><p>C:\Program Files\Wireshark&gt;tshark -r 111.pcapng -T fields -e frame.number -e ip.src -e tcp.window_size_value -e frame.time -e data.text -e tcp.analysis.duplicate_ack -e tcp.analysis.out_of_order -e tcp.analysis.retransmission -e tcp.analysis.fast_retransmission -e tcp.analysis.spurious_retransmission -e tcp.analysis.zero_window -e tcp.stream -E header=y -E separator=, -l | java JavaApplication5</p><p>also i compiled the code by using netbeans and copied JavaApplication.class file to wireshark folder and entered the mentioned command and worked</p><p>unfortunately nothing appeared in java console as you can see in this image <a href="http://www.mediafire.com/view/z26tlvl66ouzozg/Untitled3.jpg">http://www.mediafire.com/view/z26tlvl66ouzozg/Untitled3.jpg</a></p><p>any help here ?</p></div><div id="comment-38991-info" class="comment-info"><span class="comment-age">(09 Jan '15, 02:37)</span> shady</div></div><span id="38999"></span><div id="comment-38999" class="comment"><div id="post-38999-score" class="comment-score"></div><div class="comment-text"><blockquote><p>unfortunately nothing appeared in java console as you can see in this image</p></blockquote><p>If I take the Java code you posted and run the following command, it does not work either:</p><blockquote><p>echo "Hhuhu" | java JavaApplication25</p></blockquote><p>Output: -1</p><p>So, that's clearly a Java problem and not a tshark problem. Please ask your local Java guru how to fix that!</p></div><div id="comment-38999-info" class="comment-info"><span class="comment-age">(09 Jan '15, 07:02)</span> Kurt Knochner ♦</div></div><span id="39001"></span><div id="comment-39001" class="comment"><div id="post-39001-score" class="comment-score"></div><div class="comment-text"><p>ok i will thank you very much for helping me</p></div><div id="comment-39001-info" class="comment-info"><span class="comment-age">(09 Jan '15, 07:16)</span> shady</div></div></div><div id="comment-tools-38950" class="comment-tools"></div><div class="clear"></div><div id="comment-38950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

