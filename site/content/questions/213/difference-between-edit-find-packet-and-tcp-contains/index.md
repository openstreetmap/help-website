+++
type = "question"
title = "Difference between &quot;Edit -&gt; Find Packet...&quot; and &quot;tcp contains&quot;"
description = '''Hi. In the past, I have used &quot;tcp contains &amp;lt;string&amp;gt;&quot; to filter on packets containing a certain string. In the more recent past, I seem to be having problems getting this to work. Here is an example from today... With a trace file open, applying the filter [tcp contains &quot;prgetWindows&quot;] finds ze...'''
date = "2010-09-18T08:26:00Z"
lastmod = "2010-09-25T16:07:00Z"
weight = 213
keywords = [ "filter" ]
aliases = [ "/questions/213" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between "Edit -&gt; Find Packet..." and "tcp contains"](/questions/213/difference-between-edit-find-packet-and-tcp-contains)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-213-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. In the past, I have used "tcp contains &lt;string&gt;" to filter on packets containing a certain string. In the more recent past, I seem to be having problems getting this to work. Here is an example from today...</p><p>With a trace file open, applying the filter [tcp contains "prgetWindows"] finds zero packets. However, if I do Edit -&gt; Find Packet... and enter prgetWindows, as a string, I find lots of packets.</p><p>(and, Yes, the packets are TCP packets :-) )</p><p>What am I doing wrong, or not understanding?</p><p>thx all, Michael</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '10, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-213" class="comments-container"><span id="322"></span><div id="comment-322" class="comment"><div id="post-322-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the delay - a production problem has me buried. I've done more testting...</p><p>For simplicity, my search string is now "prget". Find Packet "prget" works fine. The below filters DO NOT WORK: tcp matches "[Pp][Rr][Gg][Ee][Tt]" tcp contains "prget" tds contains "prget" (It is actually TDS traffic)</p><p>I don't have a place to Post the capture file (although I could make it small enough to email), but below is a snippet of "Follow TCP Stream" output...</p><p>Thx again for any ideas.</p><p>    d b o . p r g e t W I n d o w s S e r v i c e R u n F l a g  S F ã  ?</p></div><div id="comment-322-info" class="comment-info"><span class="comment-age">(25 Sep '10, 14:12)</span> feenyman99</div></div><span id="325"></span><div id="comment-325" class="comment"><div id="post-325-score" class="comment-score"></div><div class="comment-text"><p>It might be a character encoding issue. Not sure... If you want, you can send me ([email protected]) the capture so I can have a look at it.</p></div><div id="comment-325-info" class="comment-info"><span class="comment-age">(25 Sep '10, 15:19)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-213" class="comment-tools"></div><div class="clear"></div><div id="comment-213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="327"></span>

<div id="answer-container-327" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-327-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try <code>tcp matches "p.r.g.e.t"</code>. If the traffic is TDS then strings on the wire might be encoded as UCS-2. I don't think PCRE supports UCS-2/UTF-16 but you should be able fake it for ASCII strings by adding a period between each character. You can make the match case-insensitive using the "i" flag, e.g. <code>tcp matches "(?i)p.r.g.e.t"</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '10, 16:07</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-327" class="comments-container"><span id="332"></span><div id="comment-332" class="comment"><div id="post-332-score" class="comment-score"></div><div class="comment-text"><p>OK - &lt;tcp matches="" "p.r.g.e.t"=""&gt; WORKS! And, by the way, &lt;find "p.r.g.e.t"=""&gt; does NOT. I must use &lt;find "prget"=""&gt;.<br />
</p><p>So I deduce from your helpful answers that this is a character encoding issue. Is there something I can read that will help me learn when I can use &lt;tcp contains="" "string"=""&gt; versus &lt;tcp matches="" "s.t.r.i.n.g"=""&gt;?</p><p>I have emailed a trace snippet to SYNbit, in case it's useful.</p><p>THANX to both of you for your help.</p></div><div id="comment-332-info" class="comment-info"><span class="comment-age">(26 Sep '10, 06:11)</span> feenyman99</div></div></div><div id="comment-tools-327" class="comment-tools"></div><div class="clear"></div><div id="comment-327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="214"></span>

<div id="answer-container-214" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-214-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>One difference between the find function and "tcp contains ..." is that the find function will by default use a case insensitive search. What happens when you select "case sensitive" in the find function, does it also not find any packets?</p><p>And does the filter <strong>tcp matches "[Pp][Pr][Gg][Ee][Tt][Ww][Ii][Nn][Dd][Oo][Ww][Ss]"</strong> show any packets?</p><p>If so, then it's a case issue. If not we need to look deeper, but then it would be handy to be able to look at the capture file, can you post it somewhere as this site does not (yet) have file-upload capabilities?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '10, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div></div><div id="comments-container-214" class="comments-container"><span id="451"></span><div id="comment-451" class="comment"><div id="post-451-score" class="comment-score">1</div><div class="comment-text"><p>Another difference between the "Find" function and "tcp contains" is that the "Find" function will, by default, search for characters (with codes in the range 1-255) encoded both as single-byte codes and as either big-endian or little-endian UCS-2/UTF-16 (by ignoring bytes with the value 0). As per Gerald's answer, the matching used for "XXX contains" doesn't handle UCS-2/UTF-16.</p></div><div id="comment-451-info" class="comment-info"><span class="comment-age">(06 Oct '10, 16:26)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-214" class="comment-tools"></div><div class="clear"></div><div id="comment-214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

