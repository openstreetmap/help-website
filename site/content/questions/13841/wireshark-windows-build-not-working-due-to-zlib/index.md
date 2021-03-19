+++
type = "question"
title = "Wireshark windows build not working due to ZLIB"
description = '''Hi, &quot;The windows builds might be working at buildbot (buildbot Windows-XP-x8).&quot; New developers are stopped at first point (compilation ) we are not able to download the zlib-1.2.5.zip file required for compilation. (&quot;same case for 64 Bit zlib125ws.zip&quot; ). The wget works but while unzipping it fails,...'''
date = "2012-08-23T03:58:00Z"
lastmod = "2012-08-23T06:47:00Z"
weight = 13841
keywords = [ "windows", "win32", "compilation", "build", "error" ]
aliases = [ "/questions/13841" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark windows build not working due to ZLIB](/questions/13841/wireshark-windows-build-not-working-due-to-zlib)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13841-score" class="post-score" title="current number of votes">0</div><span id="post-13841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p><strong>"The windows builds might be working at buildbot (<a href="http://buildbot.wireshark.org/trunk/builders/Windows-XP-x86">buildbot Windows-XP-x8</a>)."</strong></p><p>New developers are stopped at first point (compilation ) we are not able to download the zlib-1.2.5.zip file required for compilation. (<strong>"same case for 64 Bit zlib125ws.zip"</strong> ).</p><p>The wget works but while unzipping it fails, Its not a problem with Zip utility (tried all util's on the planet 7zip,winrar,winzip... ) non worked.</p><p>some body has messed up with the zlib kept in the trunk.</p><p>I struggled a lot to get the proper zlib-1.2.5.zip and compiled it.</p><p>Please fix it .</p><p>Build bot will not face problem because after "nmake -f Makefile.nmake setup" the script will not download using wget if the zlib-1.2.5.zip is present in "c:\wireshark-win32-libs" directory.</p><p>I tried very hard for about a week to find a proper zlib.</p><p>Regards Harsha K Gowda</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-win32" rel="tag" title="see questions tagged &#39;win32&#39;">win32</span> <span class="post-tag tag-link-compilation" rel="tag" title="see questions tagged &#39;compilation&#39;">compilation</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '12, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/0cf7e05b14ad6662ecde4c327bb2c39f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harsha&#39;s gravatar image" /><p><span>Harsha</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harsha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Aug '12, 04:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-13841" class="comments-container"><span id="13843"></span><div id="comment-13843" class="comment"><div id="post-13843-score" class="comment-score"></div><div class="comment-text"><p>Try downloading the file from below link you will face the same problem. <a href="http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2012-05-30/packages/">http://anonsvn.wireshark.org/wireshark-win32-libs/tags/2012-05-30/packages/</a></p></div><div id="comment-13843-info" class="comment-info"><span class="comment-age">(23 Aug '12, 04:09)</span> <span class="comment-user userinfo">Harsha</span></div></div></div><div id="comment-tools-13841" class="comment-tools"></div><div class="clear"></div><div id="comment-13841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13844"></span>

<div id="answer-container-13844" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13844-score" class="post-score" title="current number of votes">1</div><span id="post-13844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Works for me, using your link I'm able to download and open the zip file using 7-zip and Windows Explorer (on XP).</p><p>I've also just built on XP, deleting zlib-1.2.5.zip so ensuring setup downloaded it again with no issues.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '12, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-13844" class="comments-container"><span id="13847"></span><div id="comment-13847" class="comment"><div id="post-13847-score" class="comment-score"></div><div class="comment-text"><p>Thanks for checking . For some strange reason my firewall is blocking it. :)</p></div><div id="comment-13847-info" class="comment-info"><span class="comment-age">(23 Aug '12, 06:47)</span> <span class="comment-user userinfo">Harsha</span></div></div></div><div id="comment-tools-13844" class="comment-tools"></div><div class="clear"></div><div id="comment-13844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

