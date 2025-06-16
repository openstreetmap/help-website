+++
type = "question"
title = "Chiropractic office"
description = '''I put a node for my chiropractic office but I don&#x27;t see it on the map even after saving it. I did not find a logo/icone so I put it under amenity=doctors Can you help me figuring this out thanks'''
date = "2012-01-20T01:58:00Z"
lastmod = "2012-01-25T23:34:00Z"
weight = 10077
keywords = [ "chiropractor", "chiropratique", "chiropraticien", "chiropractic" ]
aliases = [ "/questions/10077" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Chiropractic office](/questions/10077/chiropractic-office)

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
<span id="post-10077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10077-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I put a node for my chiropractic office but I don't see it on the map even after saving it.</p>
<p>I did not find a logo/icone so I put it under <strong>amenity=doctors</strong></p>
<p>Can you help me figuring this out thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-chiropractor" rel="tag" title="see questions tagged &#39;chiropractor&#39;">chiropractor</span> <span class="post-tag tag-link-chiropratique" rel="tag" title="see questions tagged &#39;chiropratique&#39;">chiropratique</span> <span class="post-tag tag-link-chiropraticien" rel="tag" title="see questions tagged &#39;chiropraticien&#39;">chiropraticien</span> <span class="post-tag tag-link-chiropractic" rel="tag" title="see questions tagged &#39;chiropractic&#39;">chiropractic</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '12, 01:58</strong></p>
<img src="https://secure.gravatar.com/avatar/3484c447b805089613b98577733ad55e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BoneMaster&#39;s gravatar image" />
<p><span>BoneMaster</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BoneMaster has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-10077" class="comments-container">
&#10;</div>
<div id="comment-tools-10077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10077-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="10096"></span>

<div id="answer-container-10096" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10096-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-10096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There doesn't seem to be full consensus yet, but plenty of documentation : <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Healthcare">healthcare</a>, <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Healthcare_2.0">healthcare2</a>, <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Medical">medical</a>. After a quick read it seems to me that the 1st proposal is the most interesting (see also <a href="http://taginfo.openstreetmap.org/search?q=healthcare#keys">popularity on taginfo</a>). So I'd go with :</p>
<pre><code>amenity=doctors (generic, widely-recognised value for compatibility; will show an icon at least in osmarender)
healthcare=alternative
healthcare:speciality=chiropractic</code></pre>
<p>The healthcare2 proposal allows to give more details such as the physical type of facilities and the targeted population, but currently it feels a bit too unrefined to me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Jan '12, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-10096" class="comments-container">
<span id="10198"></span>
<div id="comment-10198" class="comment">
<div id="post-10198-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried your suggestion but nothing appears on the map. I only sees the node when I go to edit but not in the view windows. Can you check if I did something wrong?</p>
</div>
<div id="comment-10198-info" class="comment-info">
<span class="comment-age">(24 Jan '12, 23:12)</span> <span class="comment-user userinfo">BoneMaster</span>
</div>
</div>
<span id="10199"></span>
<div id="comment-10199" class="comment">
<div id="post-10199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We can check what you've done if you provide a "permalink" - click where it says that at the bottom right-hand corner of the map. As Vincent de P... mentioned, it'll appear on the "osmarender" map but not the "Mapnik" one. <a href="https://www.openstreetmap.org/?lat=53.99836&amp;lon=-1.05759&amp;zoom=17&amp;layers=O">Here</a>, for example, is an "amenity=doctors" on the map.</p>
</div>
<div id="comment-10199-info" class="comment-info">
<span class="comment-age">(25 Jan '12, 01:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="10219"></span>
<div id="comment-10219" class="comment">
<div id="post-10219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/?lat=46.070345&amp;lon=-72.81248&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=46.070345&amp;lon=-72.81248&amp;zoom=18&amp;layers=M</a></p>
<p>Here it is. But you won't see the node until you go into the edit mode. I will put an hospital logo juste beside it.</p>
</div>
<div id="comment-10219-info" class="comment-info">
<span class="comment-age">(25 Jan '12, 21:15)</span> <span class="comment-user userinfo">BoneMaster</span>
</div>
</div>
<span id="10220"></span>
<div id="comment-10220" class="comment">
<div id="post-10220-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The hospital logo has been saved.</p>
<p>Thanks for all your help!</p>
</div>
<div id="comment-10220-info" class="comment-info">
<span class="comment-age">(25 Jan '12, 21:18)</span> <span class="comment-user userinfo">BoneMaster</span>
</div>
</div>
<span id="10225"></span>
<div id="comment-10225" class="comment">
<div id="post-10225-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Please don't say that there is a hospital somewhere that there isn't one.<br />
</p>
<p>In an emergency someone could easily ask their satnav to "take me to the nearest hospital" and arrive on your doorstep wondering where the hospital is. As mentioned before, your office as originally added does appear on the <a href="https://www.openstreetmap.org/?lat=46.06942&amp;lon=-72.8122&amp;zoom=17&amp;layers=O">Osmarender map</a>, just not on the Mapnik one.</p>
</div>
<div id="comment-10225-info" class="comment-info">
<span class="comment-age">(25 Jan '12, 23:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10096" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10096-form-container" class="comment-form-container">
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

