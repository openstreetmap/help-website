+++
type = "question"
title = "Change Profile Configuration directory/location"
description = '''This may have already been asked and answered, but I cannot find the answer I seek, anywhere. Question:  I have multiple PC&#x27;s running Wireshark, and want to share the profile configurations across all of them. I know that I can go to [Help | About | Folders] and copy them from one PC to another, but...'''
date = "2016-01-20T17:50:00Z"
lastmod = "2017-10-06T09:02:00Z"
weight = 49419
keywords = [ "directory", "configuration", "profiles", "wireshark" ]
aliases = [ "/questions/49419" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Change Profile Configuration directory/location](/questions/49419/change-profile-configuration-directorylocation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49419-score" class="post-score" title="current number of votes">0</div><span id="post-49419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This may have already been asked and answered, but I cannot find the answer I seek, anywhere.</p><p>Question:<br />
</p><p>I have multiple PC's running Wireshark, and want to share the profile configurations across all of them. I know that I can go to [Help | About | Folders] and copy them from one PC to another, but what I would really like to do, is change the directory (folder) where those configurations are stored to be in my Dropbox directory. This way, when I make a change on one PC, it is synchronized to all of my PC's.</p><p>So, is this possible or would it be something to just add to the wishlist?</p><p>Thanks in advance, and apologize if been asked and answered somewhere else.</p><p>Travis</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-directory" rel="tag" title="see questions tagged &#39;directory&#39;">directory</span> <span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-profiles" rel="tag" title="see questions tagged &#39;profiles&#39;">profiles</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '16, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span> </br></p></div></div><div id="comments-container-49419" class="comments-container"></div><div id="comment-tools-49419" class="comment-tools"></div><div class="clear"></div><div id="comment-49419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49420"></span>

<div id="answer-container-49420" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49420-score" class="post-score" title="current number of votes">3</div><span id="post-49420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rooster_50 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you run Wireshark with the "-P persconf:path" parameter you can set the personal configuration file path, e.g if your Wireshark Dropbox directory is at d:\dropbox\wireshark:</p><pre><code>wireshark -P persconf:d:\dropbox\wireshark</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '16, 18:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jan '16, 18:17</strong> </span></p></div></div><div id="comments-container-49420" class="comments-container"><span id="49421"></span><div id="comment-49421" class="comment"><div id="post-49421-score" class="comment-score"></div><div class="comment-text"><p>Jasper, thank you so much! Exactly what I was looking for.</p></div><div id="comment-49421-info" class="comment-info"><span class="comment-age">(20 Jan '16, 18:41)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="63713"></span><div id="comment-63713" class="comment"><div id="post-63713-score" class="comment-score"></div><div class="comment-text"><p>When opening files directly by double-clicking on them (which I do a lot) it doesn't use this path. Another method I've used is to move your files to a new folder then right-click on the Wireshark preferences folder, select properties, and change the location of the folder to your new location. Essentially, I turn the Wireshark folder into a shortcut to the actual location.</p></div><div id="comment-63713-info" class="comment-info"><span class="comment-age">(06 Oct '17, 09:02)</span> <span class="comment-user userinfo">csereno</span></div></div></div><div id="comment-tools-49420" class="comment-tools"></div><div class="clear"></div><div id="comment-49420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

