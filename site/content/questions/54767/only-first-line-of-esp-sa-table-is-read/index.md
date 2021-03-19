+++
type = "question"
title = "Only First Line of ESP SA Table is Read"
description = '''I am trying to decrypt the ESP packets in both directions in Wireshark (Version 2.0.5 for OSX). I can add a single entry (SRC A --&amp;gt; DST B) to the ESP SA table and this works fine. However, when I add a second entry (SRC B --&amp;gt; DST A) for the opposite direction this entry does not work. I can ad...'''
date = "2016-08-12T03:19:00Z"
lastmod = "2016-08-14T08:31:00Z"
weight = 54767
keywords = [ "esp_sa" ]
aliases = [ "/questions/54767" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Only First Line of ESP SA Table is Read](/questions/54767/only-first-line-of-esp-sa-table-is-read)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54767-score" class="post-score" title="current number of votes">0</div><span id="post-54767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt the ESP packets in both directions in Wireshark (Version 2.0.5 for OSX). I can add a single entry (SRC A --&gt; DST B) to the ESP SA table and this works fine. However, when I add a second entry (SRC B --&gt; DST A) for the opposite direction this entry does not work. I can add the entry for SRC B --&gt; DST A as a single entry and it decrypts without issue. Is there something obvious I am missing to enable reading more than the first line in the ESP SA table?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-esp_sa" rel="tag" title="see questions tagged &#39;esp_sa&#39;">esp_sa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '16, 03:19</strong></p><img src="https://secure.gravatar.com/avatar/18a624a0f1464f37ef741d02906e28a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Walt&#39;s gravatar image" /><p><span>Walt</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Walt has no accepted answers">0%</span></p></div></div><div id="comments-container-54767" class="comments-container"><span id="54797"></span><div id="comment-54797" class="comment"><div id="post-54797-score" class="comment-score"></div><div class="comment-text"><p>Are you using the same key for both directions or different keys? And if you're using different keys, are they both correct? Also are the SPI for both directions the same or different?</p></div><div id="comment-54797-info" class="comment-info"><span class="comment-age">(14 Aug '16, 06:42)</span> <span class="comment-user userinfo">wbenton</span></div></div><span id="54800"></span><div id="comment-54800" class="comment"><div id="post-54800-score" class="comment-score"></div><div class="comment-text"><p>Yes, I am using different keys in each direction, and the SPI is also different in each direction too. I am gathering all the IPSec info for each direction using the 'ip xfrm state' command. I can decrypt either direction without issue when the SA information is in line 1 of the ESP SA table, but the second entry in the table does not seem to be read; it doesn't matter which way I add the entries to the table only the first one will be decrypted.</p></div><div id="comment-54800-info" class="comment-info"><span class="comment-age">(14 Aug '16, 08:31)</span> <span class="comment-user userinfo">Walt</span></div></div></div><div id="comment-tools-54767" class="comment-tools"></div><div class="clear"></div><div id="comment-54767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

