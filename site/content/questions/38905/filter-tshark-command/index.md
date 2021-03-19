+++
type = "question"
title = "Filter tshark command"
description = '''Hi, I&#x27;m trying to use the following command from java application:  tshark -l -T pdml -ieth0 -f &quot;host 192.168.186.128 or host 192.1.1.1&quot; -Y&quot;http&quot; When i&#x27;m executing this command line from the shell it works fine, but when i&#x27;m trying to run this command from the application i get this message: &amp;lt;?x...'''
date = "2015-01-06T08:20:00Z"
lastmod = "2015-01-07T01:33:00Z"
weight = 38905
keywords = [ "capture-filter", "tshark" ]
aliases = [ "/questions/38905" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter tshark command](/questions/38905/filter-tshark-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38905-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to use the following command from java application: tshark -l -T pdml -ieth0 -f "host 192.168.186.128 or host 192.1.1.1" -Y"http"</p><p>When i'm executing this command line from the shell it works fine, but when i'm trying to run this command from the application i get this message: &lt;?xml version="1.0"?&gt; &lt;?xml-stylesheet type="text/xsl" href="pdml2html.xsl"?&gt; &lt;pdml version="0" creator="wireshark/1.12.0" time="Tue Jan 6 18:17:43 2015" capture_file=""&gt; &lt;/pdml&gt;</p><p>Any help welcome Thanks Ilan</p></div><div id="question-tags" class="tags-container tags">capture-filter tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '15, 08:20</strong></p><img src="https://secure.gravatar.com/avatar/9c51408752862ed3bf745c88c5419ca7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ilan&#39;s gravatar image" /><p>Ilan<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ilan has no accepted answers">0%</span></p></div></div><div id="comments-container-38905" class="comments-container"></div><div id="comment-tools-38905" class="comment-tools"></div><div class="clear"></div><div id="comment-38905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38920"></span>

<div id="answer-container-38920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38920-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like your capturing process did not start. One possible reason: Your Java application does not have enough privileges to run tshark (actually dumpcap) on Linux/Unix/*BSD. If so, you will get an error message on STDERR. So, please check STDERR while you run tshark from Java to see the error message.</p><p>To fix the privilege issue, please read the following Wiki:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a><br />
</p></blockquote><p>See also my answers (and comments) to the following questions.</p><blockquote><p><a href="https://ask.wireshark.org/questions/19675/error-when-running-wireshark-on-ubuntu-as-non-root-user">https://ask.wireshark.org/questions/19675/error-when-running-wireshark-on-ubuntu-as-non-root-user</a><br />
<a href="https://ask.wireshark.org/questions/25242/wireshark-and-linux">https://ask.wireshark.org/questions/25242/wireshark-and-linux</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '15, 01:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-38920" class="comments-container"></div><div id="comment-tools-38920" class="comment-tools"></div><div class="clear"></div><div id="comment-38920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

