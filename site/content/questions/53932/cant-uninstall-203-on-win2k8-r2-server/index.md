+++
type = "question"
title = "Can&#x27;t uninstall 2.0.3 on Win2k8 R2 Server"
description = '''Good morning all, I&#x27;m currently trying to update my 2008 R2 server to the latest stable Wireshark release (2.0.4 64 bit), however I keep getting the error &quot;Wireshark or one of its associated programs is running&quot;. I&#x27;ve also tried uninstalling the current version 2.0.3 using the uninstall.exe and the ...'''
date = "2016-07-08T05:14:00Z"
lastmod = "2016-07-08T10:40:00Z"
weight = 53932
keywords = [ "rawshark", "tshark", "uninstall" ]
aliases = [ "/questions/53932" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't uninstall 2.0.3 on Win2k8 R2 Server](/questions/53932/cant-uninstall-203-on-win2k8-r2-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53932-score" class="post-score" title="current number of votes">0</div><span id="post-53932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good morning all,</p><p>I'm currently trying to update my 2008 R2 server to the latest stable Wireshark release (2.0.4 64 bit), however I keep getting the error "Wireshark or one of its associated programs is running". I've also tried uninstalling the current version 2.0.3 using the uninstall.exe and the registry uninstall string, but it says that rawshark.exe is in use. The Wireshark folder had rawshark.exe, but the uninstall.exe removed it and then states that it's in use and won't complete the uninstall process.</p><p>I've done all of the above using administrative rights on the server, and I don't see rawshark, tshark, or dumpcap running in task manager under any user on this server. What could be causing this uninstall to fail?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rawshark" rel="tag" title="see questions tagged &#39;rawshark&#39;">rawshark</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-uninstall" rel="tag" title="see questions tagged &#39;uninstall&#39;">uninstall</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '16, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/81b4de5764e2f8997da0267d3c9f91d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Woody87&#39;s gravatar image" /><p><span>Woody87</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Woody87 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '16, 06:55</strong> </span></p></div></div><div id="comments-container-53932" class="comments-container"><span id="53938"></span><div id="comment-53938" class="comment"><div id="post-53938-score" class="comment-score"></div><div class="comment-text"><p>Somewhat similar to <a href="https://ask.wireshark.org/questions/53886/wireshark-install-error">this</a> question. Can you try the suggestion in my answer there?</p></div><div id="comment-53938-info" class="comment-info"><span class="comment-age">(08 Jul '16, 07:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53945"></span><div id="comment-53945" class="comment"><div id="post-53945-score" class="comment-score"></div><div class="comment-text"><p>I've downloaded and tried the Process Explorer fix listed in the link you posted, but couldn't find anything running under "wireshark-is-running" or any other wireshark-based processes.</p></div><div id="comment-53945-info" class="comment-info"><span class="comment-age">(08 Jul '16, 10:15)</span> <span class="comment-user userinfo">Woody87</span></div></div><span id="53946"></span><div id="comment-53946" class="comment"><div id="post-53946-score" class="comment-score"></div><div class="comment-text"><p>It's not a process, but a mutex, hence the need to search for a "Handle or DLL ...".</p><p>Did you run Process Explorer as an admin, i.e. under the Process Explorer File menu there should <strong>not</strong> be an item "Show Details for All Processes"?</p></div><div id="comment-53946-info" class="comment-info"><span class="comment-age">(08 Jul '16, 10:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-53932" class="comment-tools"></div><div class="clear"></div><div id="comment-53932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

