+++
type = "question"
title = "Find Source of Spam Email"
description = '''Our ISP informed us that there is a lot of spam coming from our IP address. I am trying to use WireShark to figure out which PC it is. I did quite a big of searching and the advice is to put set the Capture Filter to port 25. So I deleted all the default filters and added a new one with filter name ...'''
date = "2011-10-19T14:16:00Z"
lastmod = "2011-10-19T17:51:00Z"
weight = 6994
keywords = [ "email" ]
aliases = [ "/questions/6994" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find Source of Spam Email](/questions/6994/find-source-of-spam-email)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6994-score" class="post-score" title="current number of votes">0</div><span id="post-6994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Our ISP informed us that there is a lot of spam coming from our IP address. I am trying to use WireShark to figure out which PC it is. I did quite a big of searching and the advice is to put set the Capture Filter to port 25. So I deleted all the default filters and added a new one with filter name = Email(Port 25) and Filter String port 25. However, it still captures a log of other traffic (NBNS, ARP, UDP, etc). Any idea how I can pinpoint the computer that sends out that spam?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-email" rel="tag" title="see questions tagged &#39;email&#39;">email</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '11, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/1b10f6ac175bfdda79f61131f6fefb97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hulu&#39;s gravatar image" /><p><span>hulu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hulu has no accepted answers">0%</span></p></div></div><div id="comments-container-6994" class="comments-container"><span id="6999"></span><div id="comment-6999" class="comment"><div id="post-6999-score" class="comment-score">1</div><div class="comment-text"><p>Where did you add the filter? Just in the capture filter list, or did you also apply it in the capture options dialog? Sounds to me like you changed your capture filter list, but probably did not actually select it for the capture itself.</p></div><div id="comment-6999-info" class="comment-info"><span class="comment-age">(19 Oct '11, 17:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-6994" class="comment-tools"></div><div class="clear"></div><div id="comment-6994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

