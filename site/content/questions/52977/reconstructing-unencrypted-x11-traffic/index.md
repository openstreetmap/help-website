+++
type = "question"
title = "Reconstructing unencrypted X11 traffic"
description = '''I have a large amount of packet capture data and a lot of it is unencrypted X11 remote screen/desktop sharing images/traffic.  However I cannot seem to get wireshark to export those streams as anything that can be read by any image viewing software. I know it is not quite that simple, but I would li...'''
date = "2016-05-26T15:57:00Z"
lastmod = "2016-05-27T15:26:00Z"
weight = 52977
keywords = [ "x11" ]
aliases = [ "/questions/52977" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reconstructing unencrypted X11 traffic](/questions/52977/reconstructing-unencrypted-x11-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52977-score" class="post-score" title="current number of votes">0</div><span id="post-52977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a large amount of packet capture data and a lot of it is unencrypted X11 remote screen/desktop sharing images/traffic.<br />
</p><p>However I cannot seem to get wireshark to export those streams as anything that can be read by any image viewing software. I know it is not quite that simple, but I would like to be able to reconstruct the images that were passed in the X11 session to demonstrate to leadership that it is possible the way the hosts are currently configured (they should be encrypting the X11 communications). I do have permission to be doing this on our network.<br />
</p><p>Any less-than-painstaking-and-eye-stabbing methods for reconstructing the screen images from the X11 packets?</p><p>Thanks for any thoughts.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-x11" rel="tag" title="see questions tagged &#39;x11&#39;">x11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '16, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/925394476287eeed3aa76a69d82ad91f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user5273&#39;s gravatar image" /><p><span>user5273</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user5273 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-52977" class="comments-container"></div><div id="comment-tools-52977" class="comment-tools"></div><div class="clear"></div><div id="comment-52977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53009"></span>

<div id="answer-container-53009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53009-score" class="post-score" title="current number of votes">0</div><span id="post-53009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not as far as I know. The X11 dissector hasn't been written to allow saving/export of images. It possibly could be but the functionality is not there now. (Some dissectors have functionality to save/export objects transferred via them--files over SMB come to mind--but X11 does not.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '16, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-53009" class="comments-container"><span id="53014"></span><div id="comment-53014" class="comment"><div id="post-53014-score" class="comment-score"></div><div class="comment-text"><p>...which means nothing more than that the hypothetical eavesdropper would need to spend some more effort than just to download Wireshark. Maybe a replay of the captured X11 stream to an X client would be enough for your purpose of demonstration to the management that the issue is serious?</p></div><div id="comment-53014-info" class="comment-info"><span class="comment-age">(27 May '16, 15:26)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-53009" class="comment-tools"></div><div class="clear"></div><div id="comment-53009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

