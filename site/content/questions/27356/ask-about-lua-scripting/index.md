+++
type = "question"
title = "ask about lua scripting"
description = '''Hi guys, i have been working in a lua dissector for a private protocol the protocol in the dump has a section with the return of the window&#x27;s API GetSystemTimeAsFileTime in the form 6a 0e 2e c2 0c e2 ce 01 this is the value of the structure FILETIME in the serve is decoded with import datetime datet...'''
date = "2013-11-25T09:25:00Z"
lastmod = "2014-03-07T16:40:00Z"
weight = 27356
keywords = [ "development", "lua", "wireshark", "bitwise", "script" ]
aliases = [ "/questions/27356" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [ask about lua scripting](/questions/27356/ask-about-lua-scripting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27356-score" class="post-score" title="current number of votes">0</div><span id="post-27356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, i have been working in a lua dissector for a private protocol</p><p>the protocol in the dump has a section with the return of the window's API GetSystemTimeAsFileTime in the form</p><p><strong>6a 0e 2e c2 0c e2 ce 01</strong></p><p>this is the value of the structure FILETIME</p><p>in the serve is decoded with</p><p>import datetime datetime.datetime.fromtimestamp((0xc22e0e6a + (0x01cee20c &lt;&lt; 32)) / 10000000.0 - 11644473600)</p><p>the hex number 0xc2220e6a is the representation of "6a 0e 2e c2" and 0x01cee20c is "0c e2 ce 01"</p><p>i tried to decoded with a lua script:</p><p>timelow = buffer(0,4):le_uint() timehihg = buffer(4,4):le_uint()</p><p>the numbers are correct (i saw it with message())</p><p>but i have problems with bit.lshift(timehigh,32)</p><p>when i did message(bit.lshift(timehigh, 32)) i got -1037169046</p><p>i think that the problem has two reasons: <em>timehigh isn't a unsigned value</em> or timehigh is a 32 bits integer without the possility to extend to 64 bits</p><p>i wanna get:</p><blockquote><blockquote><blockquote><p>"%d" % (0xc22e0e6a &lt;&lt; 32) 13992136940716032000</p></blockquote></blockquote></blockquote><p>is there any way?</p><p>p.s.: i also tried to get the complete number of 64 bits with le_uint64() but doesn't work</p><p>thanks for advance</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-bitwise" rel="tag" title="see questions tagged &#39;bitwise&#39;">bitwise</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/1b78887a0db6906cea1d126a0a9f2eac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Javier%20Aguinaga&#39;s gravatar image" /><p><span>Javier Aguinaga</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Javier Aguinaga has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '13, 09:27</strong> </span></p></div></div><div id="comments-container-27356" class="comments-container"></div><div id="comment-tools-27356" class="comment-tools"></div><div class="clear"></div><div id="comment-27356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27513"></span>

<div id="answer-container-27513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27513-score" class="post-score" title="current number of votes">0</div><span id="post-27513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>sounds like a problem with 64 bit values in Lua.</p><p>See my answer for a similar problem</p><blockquote><p><a href="http://ask.wireshark.org/questions/24594/displaying-gaps-or-drops-in-private-udp-sequence-numbers">http://ask.wireshark.org/questions/24594/displaying-gaps-or-drops-in-private-udp-sequence-numbers</a></p></blockquote><p>and the resulting bug report</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9162">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9162</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '13, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27513" class="comments-container"></div><div id="comment-tools-27513" class="comment-tools"></div><div class="clear"></div><div id="comment-27513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30588"></span>

<div id="answer-container-30588" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30588-score" class="post-score" title="current number of votes">0</div><span id="post-30588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just to bring this answer up-to-date, Wireshark now has fairly extensive 64-bit support starting in release 1.11.3. Also, the poster asked about the <code>bit.lshift()</code> operation returning a negative number: we use Mike Pall's bitop library, which always returns a <strong>signed</strong> int32 result. See <a href="http://ask.wireshark.org/questions/30478/bit-operation-returns-negative-number-that-doesnt-make-sense">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '14, 16:40</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30588" class="comments-container"></div><div id="comment-tools-30588" class="comment-tools"></div><div class="clear"></div><div id="comment-30588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

