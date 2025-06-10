+++
type = "question"
title = "CSV Export: address and geo / suppressing empty entries with osmfilter?"
description = '''Hi all, I&#x27;m currently struggling with the export of address data, checked already a bunch of discussions about here, but still found no solution... Use case: I need a bunch/huge set of addresses per country with lat, lon, country, city, street and optionally housenumber. Important is, that lat/lon i...'''
date = "2017-06-28T13:48:00Z"
lastmod = "2017-07-06T11:59:00Z"
weight = 56791
keywords = [ "dataquality", "osmfilter", "csv", "export", "addresses" ]
aliases = [ "/questions/56791" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [CSV Export: address and geo / suppressing empty entries with osmfilter?](/questions/56791/csv-export-address-and-geo-suppressing-empty-entries-with-osmfilter)

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
<span id="post-56791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56791-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I'm currently struggling with the export of address data, checked already a bunch of discussions about here, but still found no solution...</p>
<p>Use case: I need a bunch/huge set of addresses per country with lat, lon, country, city, street and optionally housenumber. Important is, that lat/lon is nearly matching to the address/street for geo selection demo content.</p>
<p>So I tried with a small test pbf (Liechtenstein) osmconvert:</p>
<p>osmconvert %1.clean.o5m --all-to-nodes --csv="<a href="https://help.openstreetmap.org/users/260/idoneus">@id</a> <a href="https://help.openstreetmap.org/users/5110/latroc">@lat</a> <a href="https://help.openstreetmap.org/users/1350/longestaugust">@lon</a> addr:country addr:postcode addr:city addr:street addr:housenumber amenity" --csv-headline --csv-separator=";" -o=%1.csv</p>
<p>Fine. After filtering in excel (sufficient in this case) the blank/incomplete entries it's what I'm looking for.</p>
<p>Next I've tried osmfilter with goal to remove exactly the same incomplete entries (of course, before I run osmconvert): osmfilter %1.o5m --keep="addr:country= and addr:city= and addr:street=" --ignore-dependencies --drop-relations --drop-ways -o=%1.clean.o5m</p>
<p>Afterwards I compared the results:</p>
<ul>
<li>osmconvert and manual filtering with excel: 91 records</li>
<li>osmfilter and osmconvert: 26 records</li>
</ul>
<p>But...</p>
<ul>
<li>Why are the results different? What does osmfilter suppress additionally? Can I use it just to suppress the empty/incomplete entries?</li>
<li>91 complete addresses is looking litte bit less for me for Liechtenstein. How can I get as much as possible valid geocode + address information like described above?</li>
<li>Is an alternative public address data set with lon, lat, country, city..., cleaned-up and best in csv format, already available?</li>
</ul>
<p>Thanks for support,</p>
<p>Regards,</p>
<p>Joerg</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dataquality" rel="tag" title="see questions tagged &#39;dataquality&#39;">dataquality</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '17, 13:48</strong></p>
<img src="https://secure.gravatar.com/avatar/967bb24c2963171b902d9cfc29f7e72b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joho68&#39;s gravatar image" />
<p><span>joho68</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joho68 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '17, 14:35</strong> </span></p>
</div>
</div>
<div id="comments-container-56791" class="comments-container">
<span id="56793"></span>
<div id="comment-56793" class="comment">
<div id="post-56793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I only find 75 with Overpass Turbo <a href="http://overpass-turbo.eu/s/q3g.">http://overpass-turbo.eu/s/q3g.</a> I suspect demanding addr:country (and even addr:city) are likely to reduce the data returned significantly. Both can often be deduced from location.</p>
</div>
<div id="comment-56793-info" class="comment-info">
<span class="comment-age">(28 Jun '17, 14:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56791-form-container" class="comment-form-container">
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

<span id="56798"></span>

<div id="answer-container-56798" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56798-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joho68 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two issues you are running in to</p>
<ul>
<li>addr:country is typically not added in "modern" OSM as we have country level admin boundaries for every country</li>
<li>90 odd addresses for LI sounds about right, neither buildings nor addresses have been mapped there in detail, see <a href="http://qa.poole.ch/?zoom=14&amp;lat=47.15743&amp;lon=9.5144&amp;layers=FTTFB0">http://qa.poole.ch/?zoom=14&amp;lat=47.15743&amp;lon=9.5144&amp;layers=FTTFB0</a></li>
</ul>
<p>Additional data on the later point: we currently have roughly half of all addresses mapped in CH, and very high coverage in AT (mostly imports there). LI simply suffers from being small and slightly away from the larger centers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '17, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '17, 18:30</strong> </span></p>
</div>
</div>
<div id="comments-container-56798" class="comments-container">
<span id="56915"></span>
<div id="comment-56915" class="comment">
<div id="post-56915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply! Tested it in meanwhile with Germany, w/o country code filtering --&gt; address quality and quantity is sufficient after clean-up, used extraction w/o osmfilter.</p>
</div>
<div id="comment-56915-info" class="comment-info">
<span class="comment-age">(06 Jul '17, 11:59)</span> <span class="comment-user userinfo">joho68</span>
</div>
</div>
</div>
<div id="comment-tools-56798" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56798-form-container" class="comment-form-container">
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

