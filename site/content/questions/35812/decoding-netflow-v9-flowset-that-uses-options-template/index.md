+++
type = "question"
title = "Decoding netflow v9 flowset that uses options template"
description = '''Hey wireshark gurus, In my captures I have got all the data templates and option templates. Then in the flowsets which contain the actual flow data, the flowset specifying the data template is decoded perfectly fine however the flowset specifying the option template is shown as &quot;no template found&quot;.....'''
date = "2014-08-27T08:54:00Z"
lastmod = "2014-08-28T13:56:00Z"
weight = 35812
keywords = [ "netflow" ]
aliases = [ "/questions/35812" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding netflow v9 flowset that uses options template](/questions/35812/decoding-netflow-v9-flowset-that-uses-options-template)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35812-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35812-score" class="post-score" title="current number of votes">0</div><span id="post-35812-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey wireshark gurus,</p><p>In my captures I have got all the data templates and option templates. Then in the flowsets which contain the actual flow data, the flowset specifying the data template is decoded perfectly fine however the flowset specifying the option template is shown as "no template found"...</p><p>Any idea where I did wrong? I am using the version 1.12.0.</p><p>Thanks! Difan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netflow" rel="tag" title="see questions tagged &#39;netflow&#39;">netflow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '14, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/08a7db94810c538eed59c44ad2601ae9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="difan&#39;s gravatar image" /><p><span>difan</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="difan has no accepted answers">0%</span></p></div></div><div id="comments-container-35812" class="comments-container"><span id="35813"></span><div id="comment-35813" class="comment"><div id="post-35813-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any idea where I did wrong?</p></blockquote><p>Maybe nothing :)</p><p>We'd have to look at the capture file to see if there's a bug (or what).</p><p>Can you post the capture file showing the issue someplace (e.g., dropbox) ?</p><p>Or: file a bug report at bugs.wireshark.org and attach the capture file to the report.</p><p>If you don't wish to have the capture file accessible by all, you can mark the bug report as private if you wish to restrict access to only the Wrieshark Core developers.</p></div><div id="comment-35813-info" class="comment-info"><span class="comment-age">(27 Aug '14, 09:07)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="35814"></span><div id="comment-35814" class="comment"><div id="post-35814-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick response! Please find the capture file at this link. <a href="https://www.dropbox.com/s/5s3oins53b5byd4/Netflow%20v9.pcapng?dl=0">https://www.dropbox.com/s/5s3oins53b5byd4/Netflow%20v9.pcapng?dl=0</a> The #3 packet contains the template. The rest packets have the "no template found" in many of them... Thanks!</p></div><div id="comment-35814-info" class="comment-info"><span class="comment-age">(27 Aug '14, 09:45)</span> <span class="comment-user userinfo">difan</span></div></div></div><div id="comment-tools-35812" class="comment-tools"></div><div class="clear"></div><div id="comment-35812-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35847"></span>

<div id="answer-container-35847" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35847-score" class="post-score" title="current number of votes">0</div><span id="post-35847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like a bug.</p><p>There's explicit code in the netflow dissector to ignore an options template if the "options scope length" is zero in the template.</p><p>However, a quick read of the Cisco V9 protocol descriptions indicates to me that an options template having an option scope length of zero is OK.</p><p>And, obviously, your capture has '0' for the options template scope length. Minor Q: What kind of equipment (router ?) generated the data in this capture ?</p><p>I'll need to do some further research, but this certainly looks like a bug.</p><p>In any case, it would be appreciated if you could file a bug at bugs.wireshark.org (attaching the capture file) so that the bug can be tracked &amp; etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '14, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '14, 12:00</strong> </span></p></div></div><div id="comments-container-35847" class="comments-container"><span id="35850"></span><div id="comment-35850" class="comment"><div id="post-35850-score" class="comment-score"></div><div class="comment-text"><p>Thanks Bill. I have created the bug report <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10432">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10432</a> It is from a Cisco 1841 router with 15.2 IOS Thanks!</p></div><div id="comment-35850-info" class="comment-info"><span class="comment-age">(28 Aug '14, 13:56)</span> <span class="comment-user userinfo">difan</span></div></div></div><div id="comment-tools-35847" class="comment-tools"></div><div class="clear"></div><div id="comment-35847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

