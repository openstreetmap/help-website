+++
type = "question"
title = "Wireshark Win32 portable installer still needs installation"
description = '''Current wireshark win32 portable installer still need installation, does, wireshark support any portable install without any effort to write windows register, and don&#x27;t need copy any files into c:windowssystem32 ?'''
date = "2010-10-17T23:05:00Z"
lastmod = "2010-10-21T23:03:00Z"
weight = 522
keywords = [ "portable", "install" ]
aliases = [ "/questions/522" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Win32 portable installer still needs installation](/questions/522/wireshark-win32-portable-installer-still-needs-installation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-522-score" class="post-score" title="current number of votes">0</div><span id="post-522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Current wireshark win32 portable installer still need installation, does, wireshark support any portable install without any effort to write windows register, and don't need copy any files into c:windowssystem32 ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-portable" rel="tag" title="see questions tagged &#39;portable&#39;">portable</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '10, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/a9b13f48d1ba3324dc29e0552dadc6ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seachange&#39;s gravatar image" /><p><span>seachange</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seachange has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Oct '10, 11:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-522" class="comments-container"></div><div id="comment-tools-522" class="comment-tools"></div><div class="clear"></div><div id="comment-522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="541"></span>

<div id="answer-container-541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-541-score" class="post-score" title="current number of votes">0</div><span id="post-541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark depends on WinPcap to capture packets on Windows. For a number of reasons the WinPcap team doesn't distribute a portable version. This makes things tricky for the PortableApps and U3 packages since the whole point is to be able run programs without modifying the system.</p><p>The best compromise so far has been to temporarily install WinPcap then uninstall it when we're done. Hopefully in the future we'll have a better solution.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '10, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Oct '10, 14:26</strong> </span></p></div></div><div id="comments-container-541" class="comments-container"><span id="580"></span><div id="comment-580" class="comment"><div id="post-580-score" class="comment-score"></div><div class="comment-text"><p>Thanks Gerald, I see, so it means we can NOT avoid installation for winpcap. IS is able to update/customize wireshark package, to locate specified winpcap DLLs from other directory(otherem then default "%systemroot%system32"), then we can copy only the DLLs of winpcap to special folder.</p><p>I tried the none interactive mode installation for normal wireshark installer with "/S" and "/D" option, but it the wireshark can NOT run with capture mode, since it can NOT find DLLs of winpcap, so I hope maybe it's possible to:</p><hr /><p>update/customize wireshark package, to locate specified winpcap DLLs from other directory(otherem then default "%systemroot%system32"), then we can copy only the DLLs of winpcap to special folder.</p></div><div id="comment-580-info" class="comment-info"><span class="comment-age">(21 Oct '10, 23:03)</span> <span class="comment-user userinfo">seachange</span></div></div></div><div id="comment-tools-541" class="comment-tools"></div><div class="clear"></div><div id="comment-541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

