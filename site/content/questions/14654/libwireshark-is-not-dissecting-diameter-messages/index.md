+++
type = "question"
title = "libwireshark is not dissecting diameter messages."
description = '''Hi, I have written an application to dissect diameter packets ,i&#x27;m using wireshark dissection engine to do it.. problem is-  I have build the application on wireshark version 1.6.5 , and the application is working fine on that system, it dissects the packets, shows the AVPs. now when i copy the appl...'''
date = "2012-10-02T22:38:00Z"
lastmod = "2012-10-03T02:33:00Z"
weight = 14654
keywords = [ "development", "libwireshark", "dissection", "diameter" ]
aliases = [ "/questions/14654" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [libwireshark is not dissecting diameter messages.](/questions/14654/libwireshark-is-not-dissecting-diameter-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14654-score" class="post-score" title="current number of votes">0</div><span id="post-14654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have written an application to dissect diameter packets ,i'm using wireshark dissection engine to do it.. problem is-</p><p>I have build the application on wireshark version 1.6.5 , and the application is working fine on that system, it dissects the packets, shows the AVPs.</p><p>now when i copy the application on another system(wireshark 1.0.8) , and i also copied the libraries from that system to another one.(libwireshark,libwsutil,libpcap etc) and i have set LD_LIBRARY_PATH to local folder containing the application.</p><p>now the application is dissecting the packets but it shows all the AVPs UNKNOWN. I just dont know what is wrong, tshark is working fine on this system but not this app.</p><p>thnks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-libwireshark" rel="tag" title="see questions tagged &#39;libwireshark&#39;">libwireshark</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '12, 22:38</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-14654" class="comments-container"><span id="14665"></span><div id="comment-14665" class="comment"><div id="post-14665-score" class="comment-score"></div><div class="comment-text"><p>the location for the dictionaries are the same.. as i copied the dictionaries to the same location as it was on previous system.</p></div><div id="comment-14665-info" class="comment-info"><span class="comment-age">(03 Oct '12, 02:19)</span> <span class="comment-user userinfo">Sanny_D</span></div></div></div><div id="comment-tools-14654" class="comment-tools"></div><div class="clear"></div><div id="comment-14654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14661"></span>

<div id="answer-container-14661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14661-score" class="post-score" title="current number of votes">0</div><span id="post-14661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>now when i copy the application on another system(wireshark 1.0.8) , and i also copied the libraries from that system to another one.(libwireshark,libwsutil,libpcap etc)</p></blockquote><p>Did you also copy the Diameter dictionaries? If not, do so. Note that they'll have to be installed in the <em>exact same location</em> as they were installed on the machine from which you copied Wireshark 1.6.5.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '12, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14661" class="comments-container"><span id="14666"></span><div id="comment-14666" class="comment"><div id="post-14666-score" class="comment-score"></div><div class="comment-text"><p>yes i did.. i also copied the diameter dictionaries to the same location on new system as it was on previous system! but still its showing it AVP UNKNOWN.</p><p>one difference i can see that is.. on previous system the libwireshark and other utils were in /usr/local/lib but on new system it is in /lib64</p></div><div id="comment-14666-info" class="comment-info"><span class="comment-age">(03 Oct '12, 02:33)</span> <span class="comment-user userinfo">Sanny_D</span></div></div></div><div id="comment-tools-14661" class="comment-tools"></div><div class="clear"></div><div id="comment-14661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

