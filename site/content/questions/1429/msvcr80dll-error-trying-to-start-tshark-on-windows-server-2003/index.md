+++
type = "question"
title = "msvcr80.dll error trying to start tshark on windows server 2003"
description = '''I tried win32 1.4.1 and 1.2.12 installers from wireshark.org. When I try to start tshark I get an error about msvcr80.dll. Notes;  the installer puts msvcr90.dll in the  Wireshark directory.  Is tshark built  in some way that is wrong for MS  server 2003? it works OK on XP.  I tried to use wireshark...'''
date = "2010-12-21T03:48:00Z"
lastmod = "2010-12-21T03:48:00Z"
weight = 1429
keywords = [ "windows", "2003", "msvcr80.dll", "tshark", "server" ]
aliases = [ "/questions/1429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [msvcr80.dll error trying to start tshark on windows server 2003](/questions/1429/msvcr80dll-error-trying-to-start-tshark-on-windows-server-2003)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1429-score" class="post-score" title="current number of votes">0</div><span id="post-1429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried win32 1.4.1 and 1.2.12 installers from wireshark.org.</p><p>When I try to start tshark I get an error about msvcr80.dll. Notes;</p><ul><li>the installer puts msvcr90.dll in the Wireshark directory.</li><li>Is tshark built in some way that is wrong for MS server 2003? it works OK on XP.</li></ul><p>I tried to use wireshark instead of tshark, as a workaround. It has similar options. however, I could not figure out how to use it in a script, as I had to press a key to get the DOS window to exit.</p><p>[edit] I have filed a bug report too.</p><p>To use wireshark, as a workaround for tshark not working, it looks like</p><pre><code>wireshark -i 2 -p -a duration:10 -k -Q -w - -z io,stat,10,ip.addr==snip &gt;&gt; %logfile% 2&gt;&amp;1</code></pre><p>should work. However, this gives major pain. The log file indicates that it is invoking tshark, which then grumbles about -k and -w not being allowed. A stack trace interspersed with strange characters follows.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-2003" rel="tag" title="see questions tagged &#39;2003&#39;">2003</span> <span class="post-tag tag-link-msvcr80.dll" rel="tag" title="see questions tagged &#39;msvcr80.dll&#39;">msvcr80.dll</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '10, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/2d84bf75137deb35d7ccd797b8df926c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20buckle&#39;s gravatar image" /><p><span>andy buckle</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy buckle has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Dec '10, 04:43</strong> </span></p></div></div><div id="comments-container-1429" class="comments-container"></div><div id="comment-tools-1429" class="comment-tools"></div><div class="clear"></div><div id="comment-1429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

