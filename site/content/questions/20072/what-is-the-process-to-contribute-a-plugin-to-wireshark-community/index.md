+++
type = "question"
title = "what is the process to contribute a plugin to wireshark community"
description = '''I want to contribute my amf plugin to wireshark community. Please provide me with the details of the contribution process'''
date = "2013-04-03T23:24:00Z"
lastmod = "2013-04-04T01:25:00Z"
weight = 20072
keywords = [ "community", "wireshark" ]
aliases = [ "/questions/20072" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [what is the process to contribute a plugin to wireshark community](/questions/20072/what-is-the-process-to-contribute-a-plugin-to-wireshark-community)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to contribute my amf plugin to wireshark community. Please provide me with the details of the contribution process</p></div><div id="question-tags" class="tags-container tags">community wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '13, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/b0ed262c234b0aa9fae2e5b2d51b14c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akhil&#39;s gravatar image" /><p>Akhil<br />
<span class="score" title="53 reputation points">53</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akhil has no accepted answers">0%</span></p></div></div><div id="comments-container-20072" class="comments-container"></div><div id="comment-tools-20072" class="comment-tools"></div><div class="clear"></div><div id="comment-20072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20074"></span>

<div id="answer-container-20074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20074-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the <a href="http://www.wireshark.org/develop.html">"Develop -&gt; Get Involved"</a> page on the Wireshark website:</p><p><em>If you have changes you want included in Wireshark, please attach it to a bug report and mark it for review.<br />
The easiest way to create a patch is to use "svn diff", e.g. svn diff &gt; my-new-protocol.patch<br />
<br />
The <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html#ChSrcSend">Developer's Guide has complete documentation</a> on preparing and uploading patches.</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '13, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-20074" class="comments-container"><span id="20078"></span><div id="comment-20078" class="comment"><div id="post-20078-score" class="comment-score"></div><div class="comment-text"><p>Note that we prefer to have the plugin converted to an internal dissector. Moreover the patch should be generated against the trunk, not 1.8 or 1.6 branches.</p></div><div id="comment-20078-info" class="comment-info"><span class="comment-age">(04 Apr '13, 05:53)</span> Pascal Quantin</div></div><span id="20080"></span><div id="comment-20080" class="comment"><div id="post-20080-score" class="comment-score"></div><div class="comment-text"><p>And fuzz test; that means collect capture files of your protocol in action and run the fuzz test tool on it. This to make sure to shake out the bugs.</p></div><div id="comment-20080-info" class="comment-info"><span class="comment-age">(04 Apr '13, 07:07)</span> Jaap ♦</div></div><span id="20081"></span><div id="comment-20081" class="comment"><div id="post-20081-score" class="comment-score"></div><div class="comment-text"><p>@Pascal Quantin, @Jaap,</p><p>Both the above points are in the developers guide section on contributions.</p></div><div id="comment-20081-info" class="comment-info"><span class="comment-age">(04 Apr '13, 07:30)</span> grahamb ♦</div></div><span id="20082"></span><div id="comment-20082" class="comment"><div id="post-20082-score" class="comment-score"></div><div class="comment-text"><p>@grahamb yes you are right: I just focused on chapter 3.9.5 and missed 3.9.4 :)</p></div><div id="comment-20082-info" class="comment-info"><span class="comment-age">(04 Apr '13, 08:45)</span> Pascal Quantin</div></div><span id="20085"></span><div id="comment-20085" class="comment"><div id="post-20085-score" class="comment-score"></div><div class="comment-text"><p>@grahamb: yes, but please do fuzz test anyway ;)</p></div><div id="comment-20085-info" class="comment-info"><span class="comment-age">(04 Apr '13, 09:29)</span> Jaap ♦</div></div></div><div id="comment-tools-20074" class="comment-tools"></div><div class="clear"></div><div id="comment-20074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

