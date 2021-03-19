+++
type = "question"
title = "&#x27;Only use the profile &quot;hosts&quot; file&#x27; Preference not working"
description = '''Hi. I&#x27;m running 1.12.5 on WIN7. I&#x27;d like to use the Wireshark Preference Only use the profile &quot;hosts&quot; file. In the About Wireshark dialog box, my Personal configuration folder is set to C:&#92;users(my id)&#92;AppData&#92;Roaming&#92;Wireshark&#92;. Inside that folder, I have a &quot;hosts&quot; file in the standard format. My N...'''
date = "2015-09-18T06:39:00Z"
lastmod = "2015-09-19T07:41:00Z"
weight = 45947
keywords = [ "hosts", "nameresolution" ]
aliases = [ "/questions/45947" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# ['Only use the profile "hosts" file' Preference not working](/questions/45947/only-use-the-profile-hosts-file-preference-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45947-score" class="post-score" title="current number of votes">0</div><span id="post-45947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I'm running 1.12.5 on WIN7. I'd like to use the Wireshark Preference <strong>Only use the profile "hosts" file</strong>. In the <strong>About Wireshark</strong> dialog box, my Personal configuration folder is set to <strong>C:\users(my id)\AppData\Roaming\Wireshark\</strong>. Inside that folder, I have a "<strong>hosts</strong>" file in the standard format. My Name Resolution preferences are:</p><ul><li>Resolve network (IP) addresses: <strong>enabled</strong></li><li>Use an external network name resolver: <strong>disabled</strong></li><li>Only use the profile "hosts" file: <strong>enabled</strong></li></ul><p>I have restarted Wireshark multiple times, obviously, but I can't get Wireshark to read the hosts file. What am I missing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span> <span class="post-tag tag-link-nameresolution" rel="tag" title="see questions tagged &#39;nameresolution&#39;">nameresolution</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '15, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/32272e9efae0156b7a71e9b634428d14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smp&#39;s gravatar image" /><p><span>smp</span><br />
<span class="score" title="39 reputation points">39</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jul '16, 15:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-45947" class="comments-container"></div><div id="comment-tools-45947" class="comment-tools"></div><div class="clear"></div><div id="comment-45947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45953"></span>

<div id="answer-container-45953" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45953-score" class="post-score" title="current number of votes">2</div><span id="post-45953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="smp has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check your profile. If you're not using the default profile, you'll need to copy the <code>hosts</code> file to the relevant profile directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '15, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-45953" class="comments-container"><span id="45956"></span><div id="comment-45956" class="comment"><div id="post-45956-score" class="comment-score"></div><div class="comment-text"><p>Bingo! Thanks!!!</p><p>Did I miss that detail in the documentation somewhere, or is the assumption that people will figure it out?</p></div><div id="comment-45956-info" class="comment-info"><span class="comment-age">(18 Sep '15, 14:37)</span> <span class="comment-user userinfo">smp</span></div></div><span id="45957"></span><div id="comment-45957" class="comment"><div id="post-45957-score" class="comment-score"></div><div class="comment-text"><p>Since my comment turned out to be the answer that resolved your question, I converted it to an answer.</p><p>I thing the documentation could be improved to make it more clear that certain files operate on a per-profile basis. After quickly scanning the user guide and man page, I don't think it's very obvious that this file works in this manner.</p></div><div id="comment-45957-info" class="comment-info"><span class="comment-age">(18 Sep '15, 14:43)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="45962"></span><div id="comment-45962" class="comment"><div id="post-45962-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. Sorry I wasn't able to get back in time to accept it myself.</p></div><div id="comment-45962-info" class="comment-info"><span class="comment-age">(19 Sep '15, 07:41)</span> <span class="comment-user userinfo">smp</span></div></div></div><div id="comment-tools-45953" class="comment-tools"></div><div class="clear"></div><div id="comment-45953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

