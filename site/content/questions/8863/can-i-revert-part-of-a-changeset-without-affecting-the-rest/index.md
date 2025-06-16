+++
type = "question"
title = "Can I revert part of a changeset without affecting the rest?"
description = '''I was adding all AH-roads in the south caucasus as relations just recently. Nevertheless, the relation https://www.openstreetmap.org/browse/relation/1770126 of the AH-81 is now empty except of one member. This happened in changeset https://www.openstreetmap.org/browse/changeset/9571754 Is it possible ...'''
date = "2011-11-07T13:16:00Z"
lastmod = "2012-02-17T10:31:00Z"
weight = 8863
keywords = [ "changeset", "revert", "relations" ]
aliases = [ "/questions/8863" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I revert part of a changeset without affecting the rest?](/questions/8863/can-i-revert-part-of-a-changeset-without-affecting-the-rest)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8863-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was adding all AH-roads in the south caucasus as relations just recently. Nevertheless, the relation <a href="https://www.openstreetmap.org/browse/relation/1770126">https://www.openstreetmap.org/browse/relation/1770126</a> of the AH-81 is now empty except of one member. This happened in changeset <a href="https://www.openstreetmap.org/browse/changeset/9571754">https://www.openstreetmap.org/browse/changeset/9571754</a></p>
<p>Is it possible to revert the changes on the relations, without reverting the rest of the changeset? It seems that user baxi does valuable contributions on the map of Azerbaijan.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '11, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '11, 20:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-8863" class="comments-container">
&#10;</div>
<div id="comment-tools-8863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8863-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8864"></span>

<div id="answer-container-8864" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8864-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8864-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8864-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible. I don't know the simplest method. The one I use involves downloading the previous version via the api as a .osm file, tweaking the version number to the current version, opening it in JOSM and checking for deleted ways, etc after downloading incomplete members, then upload.</p>
<p>I'm working on this relation for you now.</p>
<p>Edit: woodpeck_repair got there before I did. I was warned of a conflict when trying to upload the repaired relation, so checked what had changed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '11, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '11, 13:33</strong> </span></p>
</div>
</div>
<div id="comments-container-8864" class="comments-container">
<span id="8865"></span>
<div id="comment-8865" class="comment">
<div id="post-8865-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Ed, sorry, I seem to have interfered with your work - only saw this after I had already fixed the problem. I had to undelete a few ways before I would restore the relation to the last version before baxi's edit. - To the original poster: Such questions should definitely put on the mailing list and not on <a href="http://help.osm.org">help.osm.org</a> because the object-specific information in these postings is of little value for posterity!</p>
</div>
<div id="comment-8865-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 13:35)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="8866"></span>
<div id="comment-8866" class="comment">
<div id="post-8866-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No problems. I would have removed the 0 node ways (the deleted ones) from the relation when restoring, rather than undeleting them, and leave the manual checking of gaps to the original poster. Perhaps Frederik you could stick an answer on saying something like "It is possible, but such requests should be sent to &lt;list detail=""&gt;" and I'll then delete mine which is a bit lacking in detail.</p>
</div>
<div id="comment-8866-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 13:42)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="8867"></span>
<div id="comment-8867" class="comment">
<div id="post-8867-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help, guys! <em>thumbs up</em> Next time, I will ask a mailing list instead. Which one is the best for these issues?</p>
</div>
<div id="comment-8867-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 14:22)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="8868"></span>
<div id="comment-8868" class="comment">
<div id="post-8868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If it was me, I'd ask on the #OSM IRC channel. That has the advantage that everyone who might decide to help will see both the request for help and anyone saying "I'll fix it" as soon as the request and responses are made.</p>
<p>I've responded to requests for help on mailing lists before, and in one case (talk-au was being moderated at the time) the conversation was less than snappy.</p>
</div>
<div id="comment-8868-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 14:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8864" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8864-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10569"></span>

<div id="answer-container-10569" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10569-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM has a reverter plugin, and your partial revert could be accomplished with it. It can't do it exactly as you want with a few clicks, but it has the option to "revert only selected objects".</p>
<p>Basically the workflow should be as such: you would first select the relation (JOSM search allows you to select even deleted objects, if you have it loaded). Then, after the "revert selected", you would tell JOSM to download all the relation members, and remove any still deleted ways from the relation - you could even select those ways with the JOSM search - and then upload the relation only (<em>Upload selected</em> in the menu).</p>
<p>Just remember to doublecheck the outcome, before you upload the changes; as others said:</p>
<blockquote>
<p>Under no circumstances should you attempt a revert if you are not 100% sure that, should something go wrong, you can fix it again.</p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '12, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/54b673553098748d5c57bd19ae4157dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alv&#39;s gravatar image" />
<p><span>alv</span><br />
<span class="score" title="180 reputation points">180</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alv has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '12, 13:42</strong> </span></p>
</div>
</div>
<div id="comments-container-10569" class="comments-container">
<span id="10619"></span>
<div id="comment-10619" class="comment">
<div id="post-10619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another problem... in the changeset, several relations were emptied. I tried it now with relation 176922 (Asian Highway AH5), but I get the error: Upload failed, because the dataset does not fulfill one condition. Response Code = 412, Error Header=&lt;precondition failed:="" relation="" with="" id="" 176922="" cannot="" be="" saved="" due="" to="" way="" with="" id="" 127474940=""&gt;</p>
<p>The conflicting way is this one, <a href="https://www.openstreetmap.org/browse/way/127474940/history">https://www.openstreetmap.org/browse/way/127474940/history</a> a road that has later been deleted due to road construction in this area :(</p>
</div>
<div id="comment-10619-info" class="comment-info">
<span class="comment-age">(17 Feb '12, 10:11)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="10621"></span>
<div id="comment-10621" class="comment">
<div id="post-10621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Er - <a href="https://www.openstreetmap.org/browse/way/127474940/history">https://www.openstreetmap.org/browse/way/127474940/history</a> was deleted 28th Nov and says "New road in Igoeti". The coords of one node are 41.999649, 44.389927 - I doubt you can get bitterballen there!</p>
</div>
<div id="comment-10621-info" class="comment-info">
<span class="comment-age">(17 Feb '12, 10:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10569-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

