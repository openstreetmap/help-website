+++
type = "question"
title = "Removal of not:name tags"
description = '''On several occasions I have used &#x27;not:name&#x27; tags where the ITO validation site (http://www.itoworld.com/product/data/osm_analysis/main) shows a different road name from OSM, and a re-survey shows that the name in OSM is correct (e.g. according to local road signs). Sometimes it appears that the name...'''
date = "2014-07-06T22:15:00Z"
lastmod = "2014-07-09T13:14:00Z"
weight = 34681
keywords = [ "not", "tag", "name", "removal" ]
aliases = [ "/questions/34681" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Removal of not:name tags](/questions/34681/removal-of-notname-tags)

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
<span id="post-34681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On several occasions I have used 'not:name' tags where the ITO validation site (<a href="http://www.itoworld.com/product/data/osm_analysis/main)">http://www.itoworld.com/product/data/osm_analysis/main)</a> shows a different road name from OSM, and a re-survey shows that the name in OSM is correct (e.g. according to local road signs). Sometimes it appears that the name in the OS locator data is brought into line with OSM, making the 'not:name' tag unnecessary. Is it expected that 'not:name' tags will eventually be removed, and if so, how can I discover which tags are no longer needed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-removal" rel="tag" title="see questions tagged &#39;removal&#39;">removal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '14, 22:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-34681" class="comments-container">
&#10;</div>
<div id="comment-tools-34681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34681-form-container" class="comment-form-container">
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

<span id="34692"></span>

<div id="answer-container-34692" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, I had to <a href="http://wiki.openstreetmap.org/wiki/OSM_and_OSL_differences_analysis">dig into the wiki</a> to understand what the "not:name" tag is:</p>
<p>"If the name in OS Locator does not match with the name on the street, or with any other official source, then tag this using not:name=* tag. "</p>
<p>Also the <a href="http://itoworld.blogspot.ch/2010/07/new-openstreetmap-analysis-service.html">ITO's blog</a> is explaining that "If errors are found in the Ordnance Survey's data by a mapper, which do sometimes occur, then the special 'not:name' field in OpenStreetMap can be used to report this and the discrepancy will no longer appear in the above reports and mapping. Information in the 'not:name' field can also be used by the Ordnance Survey to help them improve their data quality by giving them an addition source of possible errors to check."</p>
<p>Which means that if the OS name is matching the OSM name, you just use the OSM standard "name" tag and keep only the "not:name" tag when the OS name is wrong.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '14, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-34692" class="comments-container">
<span id="34739"></span>
<div id="comment-34739" class="comment">
<div id="post-34739-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. The website that I linked in the question points out roads where the OS and OSM names are different. Where a difference resulted from an error in the OS data, and the error has then been corrected, the 'not:name' tag in OSM is no longer needed. Can anyone tell me how to find the current road name in OS open data, so that I can remove any unnecessary 'not:name' tags?</p>
</div>
<div id="comment-34739-info" class="comment-info">
<span class="comment-age">(08 Jul '14, 19:41)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="34743"></span>
<div id="comment-34743" class="comment">
<div id="post-34743-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A couple of places spring to mind - there's an "OS Locator" layer available from within Potlatch 2 (and probably other editors), which is compiled by ITO World, I believe. That shows differences only (so if a road is unnamed, or the name is the same, it won't show up). Better is <a href="http://ris.dev.openstreetmap.org/oslmusicalchairs/map?zoom=14&amp;lat=52.90326&amp;lon=-1.85826&amp;layers=B0TT&amp;view_mode=pseudorandom">Robert Scott's "Musical Chairs"</a>, which shows matches and non-matches.</p>
<p>However, I'm not convinced that removing "not:name" tags is a good idea - OS data is updated twice a year, and I've certainly seen some changes go from A to B back to A again at subsequent updates. If A is wrong and B correct, the fact that A is a not:name is worth knowing in case the OS data ever reverts.</p>
</div>
<div id="comment-34743-info" class="comment-info">
<span class="comment-age">(08 Jul '14, 21:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34759"></span>
<div id="comment-34759" class="comment">
<div id="post-34759-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can replace the "not:name" by a "note" tag explaining that the OS naming error has been fixed. It's a way the prevent someone else to "change back to A again".</p>
</div>
<div id="comment-34759-info" class="comment-info">
<span class="comment-age">(09 Jul '14, 11:15)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="34773"></span>
<div id="comment-34773" class="comment">
<div id="post-34773-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The problem with just using the "note" tag is that it doesn't appear by default in name comparison tools such as ris's. In the UK a commercial company paid a number of armchair interns to blithely copy from OS OpenData regardless of surveyed names. Initially they did a spectacularly poor job; but eventually they were trained to look at "not:name" values. Many of my name updates locally have been bucket-and-shovelling their edits.</p>
<p>A note still makes sense where there's a discrepancy, or has been a name change, or for all sorts of other reasons, but I personally wouldn't remove not:name unless the OS have actually acknowledged an error (which has happened in a few cases).</p>
</div>
<div id="comment-34773-info" class="comment-info">
<span class="comment-age">(09 Jul '14, 13:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-34692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34692-form-container" class="comment-form-container">
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

