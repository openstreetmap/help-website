+++
type = "question"
title = "getting zipcode info from OSM data"
description = '''Hello This is Sigma. It is the 1st time i am trying to use OSM.I need some data where the ZIPCodes are embedded (i.e, location available with zipcode info). I have some Tweet data and doing some researches using that data. I also want to use some OSM data (if possible) from where i can get the zipco...'''
date = "2017-07-25T20:59:00Z"
lastmod = "2017-07-28T15:12:00Z"
weight = 57272
keywords = [ "zip-code" ]
aliases = [ "/questions/57272" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [getting zipcode info from OSM data](/questions/57272/getting-zipcode-info-from-osm-data)

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
<span id="post-57272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57272-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>This is Sigma. It is the 1st time i am trying to use OSM.I need some data where the ZIPCodes are embedded (i.e, location available with zipcode info). I have some Tweet data and doing some researches using that data. I also want to use some OSM data (if possible) from where i can get the zipcode of an address (or lat/long location) and extract that zipcode with location. OSM data is more realiable than tweets. Do the addresses in OSM also provide zipcode? How can i get something useful? Any other idea?</p>
<p>Thank you for any suggestion.</p>
<p>Sigma</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zip-code" rel="tag" title="see questions tagged &#39;zip-code&#39;">zip-code</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '17, 20:59</strong></p>
<img src="https://secure.gravatar.com/avatar/125a3b54a0fa4b456031892cf23129ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sigma13&#39;s gravatar image" />
<p><span>sigma13</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sigma13 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57272" class="comments-container">
&#10;</div>
<div id="comment-tools-57272" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57272-form-container" class="comment-form-container">
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

<span id="57274"></span>

<div id="answer-container-57274" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57274-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSM data model represents zipcodes. According to <a href="https://wiki.openstreetmap.org/wiki/Addresses">relevant wiki page</a>, there are two possible representations, using the <a href="https://wiki.openstreetmap.org/wiki/Key:addr">addr:postcode</a> or <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dpostal_code">boundary:postal_code</a> keys. So, you'd want to look for objects that have the <code>addr:postcode</code> key set or that are inside a way tagged <code>boundary:postal_code</code>, depending on which convention is used in your area.</p>
<p>However, note that postcodes would only be available where they have been added to the map by someone. (Not all countries have all postcodes entered/imported into OSM.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '17, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/8440750fd002fd989ab2e6b613ca3ccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsh4&#39;s gravatar image" />
<p><span>dsh4</span><br />
<span class="score" title="867 reputation points">867</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsh4 has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-57274" class="comments-container">
<span id="57333"></span>
<div id="comment-57333" class="comment">
<div id="post-57333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much. I am looking at it right now.</p>
<p>How can i download something like that? Do i need to have QGIS?</p>
</div>
<div id="comment-57333-info" class="comment-info">
<span class="comment-age">(28 Jul '17, 15:12)</span> <span class="comment-user userinfo">sigma13</span>
</div>
</div>
</div>
<div id="comment-tools-57274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57274-form-container" class="comment-form-container">
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

