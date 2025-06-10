+++
type = "question"
title = "Mapping addresses with multiple street-like elements."
description = '''From time to time I come across addresses where there is a supplementary description between the house number and the street name. Examples, with the supplementary information in bold, are:  Unit 54, Royal Windsor Station, Thames Street, Windsor 8, The Galeb, Leen Court, Leen Gate, Nottingham  The f...'''
date = "2013-05-25T19:10:00Z"
lastmod = "2013-05-26T12:01:00Z"
weight = 22760
keywords = [ "address", "streetnames", "karlsruhe", "schema" ]
aliases = [ "/questions/22760" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping addresses with multiple street-like elements.](/questions/22760/mapping-addresses-with-multiple-street-like-elements)

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
<span id="post-22760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22760-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-22760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>From time to time I come across addresses where there is a supplementary description between the house number and the street name. Examples, with the supplementary information in bold, are:</p>
<ul>
<li>Unit 54, <strong>Royal Windsor Station</strong>, Thames Street, Windsor</li>
<li>8, <strong>The Galeb</strong>, <strong>Leen Court</strong>, Leen Gate, Nottingham</li>
</ul>
<p>The former is a retail unit in part of what was a railway station. The other is a block of flats in an old factory where each staircase of flat has a separate name: there are multiple flats sharing the no. 8 in the building, so the entire address is required.</p>
<p>I'd be interested in suggestions as to how to map these in such a way to maintain reasonable compatibility with the <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema">Karlsruhe Schema</a> other than using the <code>addr:full</code> tag.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-karlsruhe" rel="tag" title="see questions tagged &#39;karlsruhe&#39;">karlsruhe</span> <span class="post-tag tag-link-schema" rel="tag" title="see questions tagged &#39;schema&#39;">schema</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '13, 19:10</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 May '13, 03:55</strong> </span></p>
</div>
</div>
<div id="comments-container-22760" class="comments-container">
&#10;</div>
<div id="comment-tools-22760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22760-form-container" class="comment-form-container">
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

<span id="22761"></span>

<div id="answer-container-22761" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22761-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The bold parts are names of (parts of) buildings, so I would put them in the addr:housename tag. I wouldn't worry too much about the "or" in the proposal in "housename or housenumber", as I can't find the "or" on the <a href="http://wiki.openstreetmap.org/wiki/Key:addr">feature page</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '13, 19:46</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-22761" class="comments-container">
<span id="22766"></span>
<div id="comment-22766" class="comment">
<div id="post-22766-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK how about 1, Naranjan Mews, Gedling Grove (where Mews is a short side street, but the main street Gedling Grove is still part of the address). On OSM <a href="http://osm.org/go/eu8ZpEkZr--.">http://osm.org/go/eu8ZpEkZr--.</a></p>
</div>
<div id="comment-22766-info" class="comment-info">
<span class="comment-age">(25 May '13, 20:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="22770"></span>
<div id="comment-22770" class="comment">
<div id="post-22770-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If both parts are streets and both are part of the official address then IMHO both belong in addr:street. I.e.: addr:street=Naranjan Mews, Gedling Grove</p>
</div>
<div id="comment-22770-info" class="comment-info">
<span class="comment-age">(25 May '13, 23:15)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-22761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22761-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22768"></span>

<div id="answer-container-22768" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22768-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Karlsruhe Schema you linked has a tag named addr:full which is already often used in GB.<br />
Example: <a href="http://overpass-turbo.eu/s/eE">London</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '13, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></p>
</div>
</div>
<div id="comments-container-22768" class="comments-container">
<span id="22773"></span>
<div id="comment-22773" class="comment">
<div id="post-22773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have amended the question to add, other than using addr:full!</p>
</div>
<div id="comment-22773-info" class="comment-info">
<span class="comment-age">(26 May '13, 03:54)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="22778"></span>
<div id="comment-22778" class="comment">
<div id="post-22778-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Why would you prefer to not use this tag?</p>
</div>
<div id="comment-22778-info" class="comment-info">
<span class="comment-age">(26 May '13, 10:08)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="22779"></span>
<div id="comment-22779" class="comment">
<div id="post-22779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't mind using this tag, and I already knew about it and have used it, so didn't need to ask a question about it. (Of course your answer is useful for anyone who did not know about addr:full).</p>
<p>I would prefer a tagging scheme which did not require complex address parsing in any post-processing. A significant goal is to be able to provide an open equivalent of the UK Postal Address File (PAF), see Matt Williams' Postcode Finder <a href="http://milliams.dev.openstreetmap.org/postcodefinder/about/.">http://milliams.dev.openstreetmap.org/postcodefinder/about/.</a></p>
</div>
<div id="comment-22779-info" class="comment-info">
<span class="comment-age">(26 May '13, 12:01)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22768-form-container" class="comment-form-container">
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

