+++
type = "question"
title = "How does one tag a complex opening_hours, in America?"
description = '''I would like to know how to tag this opening hours by using this tool http://openingh.openstreetmap.de/evaluation_tool/ . I don&#x27;t know how to successful tag it with all the ending hours of the week ending at 01:00 in the morning. Thanks MONDAY: 6:00AM - 1:00AM TUESDAY: 6:00AM - 1:00AM WEDNESDAY: 6:0...'''
date = "2014-06-02T09:24:00Z"
lastmod = "2014-06-03T07:51:00Z"
weight = 33614
keywords = [ "opening_hours" ]
aliases = [ "/questions/33614" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How does one tag a complex opening_hours, in America?](/questions/33614/how-does-one-tag-a-complex-opening_hours-in-america)

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
<span id="post-33614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33614-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to know how to tag this opening hours by using this tool <a href="http://openingh.openstreetmap.de/evaluation_tool/">http://openingh.openstreetmap.de/evaluation_tool/</a> . I don't know how to successful tag it with all the ending hours of the week ending at 01:00 in the morning. Thanks</p>
<p>MONDAY: 6:00AM - 1:00AM</p>
<p>TUESDAY: 6:00AM - 1:00AM</p>
<p>WEDNESDAY: 6:00AM - 1:00AM</p>
<p>THURSDAY: 6:00AM - 1:00AM</p>
<p>FRIDAY: 6:00AM - 6:00AM</p>
<p>SATURDAY: 6:00AM - 6:00AM</p>
<p>SUNDAY: 6:00AM - 1:00AM</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '14, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c592fa30e4ddc999332a3ebf440e1d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frankthetankk&#39;s gravatar image" />
<p><span>frankthetankk</span><br />
<span class="score" title="106 reputation points">106</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frankthetankk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '14, 09:25</strong> </span></p>
</div>
</div>
<div id="comments-container-33614" class="comments-container">
<span id="33617"></span>
<div id="comment-33617" class="comment">
<div id="post-33617-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What's "6:00AM - 6:00AM" supposed to mean? Opened until the next day? Or just for 60 seconds? :)</p>
</div>
<div id="comment-33617-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 09:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33614-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="33619"></span>

<div id="answer-container-33619" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33619-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For now I excluded your odd opening hours for Friday and Saturday.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/Key:opening_hours:specification">opening hours specification</a> states: "If the second time is earlier then the first one, it is assumed to be on the next day.". Therefore specifying a time range which includes the next day is perfectly valid:</p>
<pre><code>Mo-Th 06:00-01:00; Su 06:00-01:00</code></pre>
<p>Alternatively you could just specify the opening hours for each day separately. It will look more complicated but means exactly the same:</p>
<pre><code>Mo-Th 00:00-01:00,06:00-24:00; Fr 00:00-01:00; Su 06:00-24:00</code></pre>
<p>There is also a nice plugin for JOSM: <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpeningHoursEditor">OpeningHoursEditor</a>. It makes editing opening hours quite easy. But always double-check the result, there are some bugs and it doesn't support the whole opening hours specification.</p>
<p>Also see the <a href="http://openingh.openstreetmap.de/evaluation_tool/">opening hours evaluation tool</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '14, 10:17</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '14, 10:18</strong> </span></p>
</div>
</div>
<div id="comments-container-33619" class="comments-container">
<span id="33635"></span>
<div id="comment-33635" class="comment">
<div id="post-33635-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for trying to help. I already linked the opening hours evaluation tool above and was having problems getting the correct outcome. Plus you left out Saturday. Your code didn't seem to work out.</p>
</div>
<div id="comment-33635-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 22:41)</span> <span class="comment-user userinfo">frankthetankk</span>
</div>
</div>
<span id="33638"></span>
<div id="comment-33638" class="comment">
<div id="post-33638-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I left out Friday and Saturday because <em>6:00AM - 6:00AM</em> didn't make any sense to me and you didn't react to my comment asking about clarification.</p>
</div>
<div id="comment-33638-info" class="comment-info">
<span class="comment-age">(03 Jun '14, 07:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33619-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33620"></span>

<div id="answer-container-33620" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33620-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Past midnight, it's the next day. So add the 0-1am section in the next day. You can have multiple sections per day. This is explained in the <a href="https://wiki.openstreetmap.org/wiki/Opening_hours">wiki</a>. Assuming you mean that this POI is open 24h on friday and saturday, it gives:</p>
<pre><code>Mo-Su 00:00-01:00,18:00-24:00; Fr,Sa 00:00-24:00</code></pre>
<p>You may find the josm plugin easyer to use than this webpage.</p>
<p>As a side note, avoid using the 12h format unless you absolutely need to. It's confusing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '14, 10:23</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-33620" class="comments-container">
<span id="33636"></span>
<div id="comment-33636" class="comment">
<div id="post-33636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for trying to help. Your code didn't work out the way I asked in the question above.</p>
</div>
<div id="comment-33636-info" class="comment-info">
<span class="comment-age">(02 Jun '14, 22:42)</span> <span class="comment-user userinfo">frankthetankk</span>
</div>
</div>
</div>
<div id="comment-tools-33620" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33620-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33637"></span>

<div id="answer-container-33637" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33637-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Mo-Fr 00:00-01:00,06:00-24:00; Sa,Su 00:00-24:00</p>
<p>I figured out the correct opening hours on my own from using the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpeningHoursEditor">OpeningHoursEditor</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '14, 22:44</strong></p>
<img src="https://secure.gravatar.com/avatar/c592fa30e4ddc999332a3ebf440e1d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frankthetankk&#39;s gravatar image" />
<p><span>frankthetankk</span><br />
<span class="score" title="106 reputation points">106</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frankthetankk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33637" class="comments-container">
&#10;</div>
<div id="comment-tools-33637" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33637-form-container" class="comment-form-container">
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

