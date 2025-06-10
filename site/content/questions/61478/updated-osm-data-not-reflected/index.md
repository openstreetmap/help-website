+++
type = "question"
title = "Updated osm data not reflected"
description = '''hi, I have updated an OSM data (osm_id: 5319742462) as suburb:Valasaravakkam. http://www.openstreetmap.org/node/5319742462 But still, I got incorrect old data as suburb:Virugambakkam. http://nominatim.openstreetmap.org/lookup?osm_ids=N5319742462'''
date = "2018-01-04T11:31:00Z"
lastmod = "2018-01-05T23:40:00Z"
weight = 61478
keywords = [ "editing", "data", "update", "nominatim" ]
aliases = [ "/questions/61478" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Updated osm data not reflected](/questions/61478/updated-osm-data-not-reflected)

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
<span id="post-61478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61478-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi,</p>
<p>I have updated an OSM data (osm_id: 5319742462) as suburb:Valasaravakkam.</p>
<p><a href="http://www.openstreetmap.org/node/5319742462">http://www.openstreetmap.org/node/5319742462</a></p>
<p>But still, I got incorrect old data as suburb:Virugambakkam.</p>
<p><a href="http://nominatim.openstreetmap.org/lookup?osm_ids=N5319742462">http://nominatim.openstreetmap.org/lookup?osm_ids=N5319742462</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '18, 11:31</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jan '18, 19:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-61478" class="comments-container">
&#10;</div>
<div id="comment-tools-61478" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61478-form-container" class="comment-form-container">
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

<span id="61485"></span>

<div id="answer-container-61485" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61485-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>AFAIK, Nominatim ignores any address information on the node except for the postal code and house number.</p>
<p>See the <a href="https://wiki.openstreetmap.org/wiki/Nominatim/FAQ#How_was_the_address_calculated.3F">FAQ</a> of Nominatim on how you can fix an incorrect address. It says that you have to add a node or area, it does not mention that you can change it by adding addr:suburb.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '18, 20:02</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-61485" class="comments-container">
<span id="61492"></span>
<div id="comment-61492" class="comment">
<div id="post-61492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Added a new data with correct address details, but still, nominatim shows incorrect data. <a href="http://www.openstreetmap.org/node/5321788696">http://www.openstreetmap.org/node/5321788696</a></p>
<p><a href="http://nominatim.openstreetmap.org/lookup?osm_ids=N5321788696">http://nominatim.openstreetmap.org/lookup?osm_ids=N5321788696</a></p>
</div>
<div id="comment-61492-info" class="comment-info">
<span class="comment-age">(05 Jan '18, 10:45)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="61494"></span>
<div id="comment-61494" class="comment">
<div id="post-61494-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>With <a href="http://nominatim.openstreetmap.org/details.php?place_id=223951484">http://nominatim.openstreetmap.org/details.php?place_id=223951484</a> you can see how the address is constructed. I got this URL by typing "3S Touch Service Solutions Private Limited" on the search box of <a href="http://nominatim.openstreetmap.org">http://nominatim.openstreetmap.org</a></p>
<p>I do not understand "Added a new data with correct address details". Did you add a node for the Valasaravakkam suburb ? If not, you have to do that, tweaking the node representing your company won't help. In case you added the node, it only works when it's closer than the other suburb nodes. So you could move the suburb node a bit, but probably break other addresses. Adding an area for the suburb is really the best solution.</p>
</div>
<div id="comment-61494-info" class="comment-info">
<span class="comment-age">(05 Jan '18, 10:54)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="61499"></span>
<div id="comment-61499" class="comment">
<div id="post-61499-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The node for <a href="http://www.openstreetmap.org/node/294073565">Valasaravakkam</a> is tagged as a town, not a suburb. Therefore, Virugambakkam is the closest suburb and that's why nominatim is saying what it is.</p>
</div>
<div id="comment-61499-info" class="comment-info">
<span class="comment-age">(05 Jan '18, 23:40)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-61485" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61485-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61484"></span>

<div id="answer-container-61484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61484-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span class="small">(Update: while this is still true and should be kept in mind when troubleshooting, it is likely <em>not</em> the reason for the issue here)</span></p>
<p>Nominatim has a different database. It needs some time to update it. Your question was just very few hours after your edit. Try again tomorrow.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '18, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '18, 18:56</strong> </span></p>
</div>
</div>
<div id="comments-container-61484" class="comments-container">
&#10;</div>
<div id="comment-tools-61484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61484-form-container" class="comment-form-container">
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

