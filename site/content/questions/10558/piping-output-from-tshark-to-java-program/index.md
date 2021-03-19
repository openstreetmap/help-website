+++
type = "question"
title = "Piping output from tshark to Java program"
description = '''Lets say that the tshark command for piping the output from tshark is : tshark -i your_interface -n | your_program I would like to pipe the output from tshark to the java program. I compiled the java file and i piped the tshark output to the java program like this : tshark -i 1 -n | java &quot;C:&#92;Users&#92;L...'''
date = "2012-05-01T18:13:00Z"
lastmod = "2012-05-01T21:56:00Z"
weight = 10558
keywords = [ "pipe", "java", "tshark" ]
aliases = [ "/questions/10558" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Piping output from tshark to Java program](/questions/10558/piping-output-from-tshark-to-java-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10558-score" class="post-score" title="current number of votes">0</div><span id="post-10558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Lets say that the tshark command for piping the output from tshark is :</p><p>tshark -i your_interface -n | your_program</p><p>I would like to pipe the output from tshark to the java program.</p><p>I compiled the java file and i piped the tshark output to the java program like this :</p><p><code>tshark -i 1 -n | java "C:\Users\L33604\Desktop\Eclipse Indigo x64-Bit\eclipse\project workspace\Splunk Project\src\Program.class"</code></p><p>The error was thrown :</p><p><code>could not find or load main class  : C:\\..... tshark an error occurred while printing packets : invalid arguement.</code></p><p>The question is what is the way to pipe the tshark output to the java program using tshark command?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '12, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p><span>misteryuku</span><br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 May '12, 23:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10558" class="comments-container"></div><div id="comment-tools-10558" class="comment-tools"></div><div class="clear"></div><div id="comment-10558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10559"></span>

<div id="answer-container-10559" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10559-score" class="post-score" title="current number of votes">0</div><span id="post-10559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"could not find or load main class" is a Java error; there's something wrong with your program or with the way you're running it with the "java" command. I can't help you with that.</p><p>"an error occurred while printing packets : invalid argument" may just be an error given when TShark tries to write to a pipe when the program on the other side of the pipe has terminated.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '12, 19:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10559" class="comments-container"></div><div id="comment-tools-10559" class="comment-tools"></div><div class="clear"></div><div id="comment-10559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10564"></span>

<div id="answer-container-10564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10564-score" class="post-score" title="current number of votes">0</div><span id="post-10564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>---- "could not find or load main class"</p><p>As already mentioned, there is something wrong with your java class file, most certainly the main method is missing in your class file. I think you will get more detailed information in a Java forum.</p><p>Here is a working example:</p><p>Echo.java</p><p><code> import java.io.*;</code></p><code></code><p><code>public class Echo {   public static void main(String[] args) throws IOException {     BufferedReader in = new BufferedReader(new InputStreamReader(System.in));     String s;     while ((s = in.readLine()) != null &amp;&amp; s.length() != 0)       System.out.println(s);     // An empty line or Ctrl-Z terminates the program   } } ///:~</code></p><p>Compile it: javac Echo.java</p><p>Run it: tshark -i 1 -n | java Echo</p><p>Note: just 'java Echo' not 'java Echo.class', as it would expect a main method then!</p><p>Output:</p><p>Capturing on VMware Accelerated AMD PCNet Adapter (Microsoft's Packet Scheduler)<br />
0.000000 192.168.30.142 -&gt; 192.168.30.2 ICMP 74 Echo (ping) request id=0x0200, seq=15106/571, ttl=128<br />
0.000116 192.168.30.2 -&gt; 192.168.30.142 ICMP 74 Echo (ping) reply id=0x0200, seq=15106/571, ttl=128<br />
</p><p>Hint: This is buffered input stream reading, so it take some time until the code prints something on the CLI (the buffer needs to be filled first).</p><p>---- "tshark an error occurred while printing packets : invalid arguement"</p><p>I have no idea where that comes from. Does this work without errors on your system: tshark -i 1 -n</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '12, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-10564" class="comments-container"></div><div id="comment-tools-10564" class="comment-tools"></div><div class="clear"></div><div id="comment-10564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

