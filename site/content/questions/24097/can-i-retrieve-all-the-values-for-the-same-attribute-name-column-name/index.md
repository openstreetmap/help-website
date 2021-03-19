+++
type = "question"
title = "Can I retrieve all the values for the same attribute name (Column name)?"
description = '''Hi ,  Currently I am having a .pcap file with the below sample data. Just showing in an xml format.. &amp;lt;packet&amp;gt; &amp;lt;field name=&quot;radius.Class&quot; show=&quot;ABC&quot; value=&quot;ABC&quot;/&amp;gt; &amp;lt;/field&amp;gt; &amp;lt;field name=&quot;radius.Class&quot; show=&quot;DEF&quot; value=&quot;DEF&quot;/&amp;gt; &amp;lt;/field&amp;gt; &amp;lt;field name=&quot;radius.Class&quot; show=&quot;HI...'''
date = "2013-08-27T07:17:00Z"
lastmod = "2013-08-27T09:53:00Z"
weight = 24097
keywords = [ "column", "field", "commandline", "tshark" ]
aliases = [ "/questions/24097" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Can I retrieve all the values for the same attribute name (Column name)?](/questions/24097/can-i-retrieve-all-the-values-for-the-same-attribute-name-column-name)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24097-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>Currently I am having a .pcap file with the below sample data. Just showing in an xml format..</p>&lt;packet&gt; &lt;field name="radius.Class" show="ABC" value="ABC"/&gt; &lt;/field&gt; &lt;field name="radius.Class" show="DEF" value="DEF"/&gt; &lt;/field&gt; &lt;field name="radius.Class" show="HIJ" value="HIJ"/&gt; &lt;/field&gt; &lt;/packet&gt;<p>The tshark command that I am using currently is</p><p><strong>tshark -r "PCAP Input file location" -T fields -e radius.Class -E separator=, -E header=y &gt; output.csv</strong></p><p>Current result on Windows OS</p><p><strong>radius.Class<br />
ABC DEF HIJ</strong></p><p>But for the same command on centOS or Linux I am getting only the last column as shown below</p><p><strong>radius.Class</strong></p><p><strong>HIJ</strong></p><p>For some reason it is retrieving only the last attribute value. Is there any way that I can retrieve all the columns on centOS or Linux ???</p></div><div id="question-tags" class="tags-container tags">column field commandline tshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '13, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/a65ec1a7a48d2fc43b453bc6175bed34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sunny%20Reddy&#39;s gravatar image" /><p>Sunny Reddy<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sunny Reddy has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '14, 22:39</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-24097" class="comments-container"></div><div id="comment-tools-24097" class="comment-tools"></div><div class="clear"></div><div id="comment-24097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24103"></span>

<div id="answer-container-24103" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24103-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Which tshark version are you using on both systems, there have been changes in behavior between versions.</p><p>In recent versions you can use the option <code>"-E occurrence=a"</code> to print all fields and use <code>"-E aggregator=&lt;char&gt;"</code> to choose how the fields should be separated.</p><p>See tshark -h for more info...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '13, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-24103" class="comments-container"><span id="24108"></span><div id="comment-24108" class="comment"><div id="post-24108-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help..</p><p>Sorry forgot to mention it</p><p>TShark 1.0.15</p><p>Copyright 1998-2010 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled with GLib 2.12.3, with libpcap 0.9.4, with libz 1.2.3, without POSIX capabilities, with libpcre 6.6, with SMI 0.4.5, without ADNS, without Lua, with GnuTLS 1.4.1, with Gcrypt 1.4.4, with MIT Kerberos.</p><p>Running on Linux 2.6.18-308.16.1.el5, with libpcap version 0.9.4.</p><p>Built using gcc 4.1.2 20080704 (Red Hat 4.1.2-54).</p></div><div id="comment-24108-info" class="comment-info"><span class="comment-age">(27 Aug '13, 10:12)</span> Sunny Reddy</div></div><span id="24111"></span><div id="comment-24111" class="comment"><div id="post-24111-score" class="comment-score"></div><div class="comment-text"><p>Hi SYN-bit, Tried doing that but I am getting the below error</p><p>tshark: " occurence" is not a valid field output option=value pair. TShark: The available options for field output "E" are: header=y|n Print field abbreviations as first line of output (def: N: no) separator=/t|/s|&lt;character&gt; Set the separator to use; "/t" = tab, "/s" = space (def: /t: tab) quote=d|s|n Print either d: double-quotes, s: single quotes or n: no quotes around field values (def: n: none)</p></div><div id="comment-24111-info" class="comment-info"><span class="comment-age">(27 Aug '13, 11:08)</span> Sunny Reddy</div></div><span id="24112"></span><div id="comment-24112" class="comment"><div id="post-24112-score" class="comment-score"></div><div class="comment-text"><p>@Sunny Reddy, your version (1.0.15) is very ancient and doesn't qualify as a "recent version" as per the answer from @SYN-bit.</p></div><div id="comment-24112-info" class="comment-info"><span class="comment-age">(27 Aug '13, 11:24)</span> grahamb ♦</div></div><span id="24113"></span><div id="comment-24113" class="comment"><div id="post-24113-score" class="comment-score"></div><div class="comment-text"><p>I think I added the "occurrence" output option in 1.4. So yes, you can get all the values of radius.Class on linux, but you will have to upgrade tshark. If 1.0.15 is the one from the repository, then you will have to compile a newer version yourself or switch to a more recent OS version with a more recent tshark version.</p></div><div id="comment-24113-info" class="comment-info"><span class="comment-age">(27 Aug '13, 11:58)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-24103" class="comment-tools"></div><div class="clear"></div><div id="comment-24103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

