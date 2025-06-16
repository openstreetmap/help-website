+++
type = "question"
title = "Rearranging XML to Excel data - have a column show up twice"
description = '''Hi there. I would like to rearrange xml files in excel in the following format: lat | long | k | v | v If you are familiar with the xml schema I cant repeat column v twice. Essentially what I want to do is make an excel file for all restaurants with lat, long, name and cuisine.'''
date = "2011-07-04T10:59:00Z"
lastmod = "2012-09-19T00:11:00Z"
weight = 6167
keywords = [ "xml", "csv", "export" ]
aliases = [ "/questions/6167" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Rearranging XML to Excel data - have a column show up twice](/questions/6167/rearranging-xml-to-excel-data-have-a-column-show-up-twice)

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
<span id="post-6167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6167-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there.</p>
<p>I would like to rearrange xml files in excel in the following format:</p>
<p>lat | long | k | v | v</p>
<p>If you are familiar with the xml schema I cant repeat column v twice. Essentially what I want to do is make an excel file for all restaurants with lat, long, name and cuisine.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '11, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/5c8b9c96fdc4d80e3e198f3268a159f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bulleh&#39;s gravatar image" />
<p><span>bulleh</span><br />
<span class="score" title="14 reputation points">14</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bulleh has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '11, 15:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span></p>
</div>
</div>
<div id="comments-container-6167" class="comments-container">
&#10;</div>
<div id="comment-tools-6167" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6167-form-container" class="comment-form-container">
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

<span id="6169"></span>

<div id="answer-container-6169" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6169-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Ruby library <strong><a href="http://osmlib.rubyforge.org">OSMlib</a></strong> allows <a href="http://osmlib.rubyforge.org/osmlib-export/rdoc/files/doc/format-csv.html">export into CSV</a>.</p>
<p>The example in the documentation pointed to above has a hospital example that mirrors your restaurant example.</p>
<p>One thing to be aware of, as it sounds like you're looking to extract the data out of OSM, is that the license persists, and your new dataset in CSV form is still under the CC-BY-SA license (until OSM completes the license transition).</p>
<p>So if you distribute this file, it must be under the terms of the CC-BY-SA. If you make a new map, it's a derived work, and if you combine this data with other data, it's a derived work. You should read the various license pages on the OSM Wiki for more information about this, in particular the page on <a href="https://wiki.openstreetmap.org/wiki/Common_licence_interpretations">Common license interpretations</a> may help.</p>
<p>OSM's a great resource for POI data. Good luck with your project!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '11, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jul '11, 15:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-6169" class="comments-container">
&#10;</div>
<div id="comment-tools-6169" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6169-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6170"></span>

<div id="answer-container-6170" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6170-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not that it's really anything to do with OSM, but the Excel data import wizard will import one row per tag combination. You can tell which tags are for the same item by looking at the "id" column.</p>
<p>How to rearrange the data in Excel is a question best asked somewhere like <a href="http://social.technet.microsoft.com/Forums/en/excel/threads">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jul '11, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-6170" class="comments-container">
&#10;</div>
<div id="comment-tools-6170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6170-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16247"></span>

<div id="answer-container-16247" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16247-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Meanwhile the newly introduced <code>--csv</code> option of <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Writing_CSV_Files">osmconvert</a> will help you to create CSV files rather easily. For example:</p>
<pre><code>./osmconvert shops.osm --all-to-nodes --csv=&quot;@id @lon @lat amenity shop name&quot; --csv-headline
@id               @lon        @lat        amenity  shop       name
21548298          11.6122123  48.6884848  shop     bakery     Miller
21552613          9.0651970   49.9979332  shop     butcher    Jaeger
1000000168276611  6.6058085   51.4556093  shop     drugstore  AllForYou</code></pre>
<p>To filter all restaurants out of an OSM file you may use <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '12, 00:11</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-16247" class="comments-container">
&#10;</div>
<div id="comment-tools-16247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16247-form-container" class="comment-form-container">
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

