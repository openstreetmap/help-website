+++
type = "question"
title = "Error when creating .exe with NSIS"
description = '''I am trying to create a windows installer which includes some custom plugins. I can build without error, but when I try to create an nsis .exe using the line &quot;nmake -f makefile.nmake packaging&quot; I encounter the following error: File: &quot;C:&#92;Wireshark-win64-libs-1.10&#92;vcredist_x64.exe&quot; -&amp;gt; no files foun...'''
date = "2014-06-04T07:18:00Z"
lastmod = "2014-06-04T07:56:00Z"
weight = 33379
keywords = [ "nsis", "windows7", "vcredist", "64-bit", "installer" ]
aliases = [ "/questions/33379" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Error when creating .exe with NSIS](/questions/33379/error-when-creating-exe-with-nsis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33379-score" class="post-score" title="current number of votes">0</div><span id="post-33379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to create a windows installer which includes some custom plugins. I can build without error, but when I try to create an nsis .exe using the line "nmake -f makefile.nmake packaging" I encounter the following error:</p><pre><code>File: &quot;C:\Wireshark-win64-libs-1.10\vcredist_x64.exe&quot; -&gt; no files found.
Usage: File [/nonfatal] [/a] ([/r] [/x filespec [...]] filespec [...] | /oname=outfile one_file_only)
Error in script &quot;wireshark.nsi&quot; on line 369 -- aborting creation process
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\NSIS\makensis.exe&quot;&#39; : return code &#39;0x1&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\amd64\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>I am building from the Wireshark-1.10.7.tar.bz2 from the wireshark website and am using Windows 7 x64. What can I do about this error?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nsis" rel="tag" title="see questions tagged &#39;nsis&#39;">nsis</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-vcredist" rel="tag" title="see questions tagged &#39;vcredist&#39;">vcredist</span> <span class="post-tag tag-link-64-bit" rel="tag" title="see questions tagged &#39;64-bit&#39;">64-bit</span> <span class="post-tag tag-link-installer" rel="tag" title="see questions tagged &#39;installer&#39;">installer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '14, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/8f51fdd676352de28608f014b75acbcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20G&#39;s gravatar image" /><p><span>Thomas G</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas G has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jun '14, 07:21</strong> </span></p></div></div><div id="comments-container-33379" class="comments-container"></div><div id="comment-tools-33379" class="comment-tools"></div><div class="clear"></div><div id="comment-33379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33381"></span>

<div id="answer-container-33381" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33381-score" class="post-score" title="current number of votes">2</div><span id="post-33381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Thomas G has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you have to download the aproprate</p><p>File: "C:\Wireshark-win64-libs-1.10\vcredist_x64.exe</p><p>for your visual studio version and put it in the above directory. I think this is mentioned in the guide.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-33381" class="comments-container"><span id="33385"></span><div id="comment-33385" class="comment"><div id="post-33385-score" class="comment-score"></div><div class="comment-text"><p>Thank you, that was the problem.</p></div><div id="comment-33385-info" class="comment-info"><span class="comment-age">(04 Jun '14, 07:56)</span> <span class="comment-user userinfo">Thomas G</span></div></div></div><div id="comment-tools-33381" class="comment-tools"></div><div class="clear"></div><div id="comment-33381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

