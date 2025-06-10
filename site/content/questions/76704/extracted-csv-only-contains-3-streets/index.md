+++
type = "question"
title = "Extracted csv only contains 3 streets"
description = '''I&#x27;m trying to extract the street name of a city from an osm file (converted from pbf) that I got from geofabrik. I used osmfilter and osmconvert for the extraction, using this command: osmfilter indonesia-latest.osm --keep=&quot;addr:country= and addr:city=Bandung and addr:street=&quot; --ignore-dependencies ...'''
date = "2020-09-19T03:21:00Z"
lastmod = "2020-10-08T10:36:00Z"
weight = 76704
keywords = [ "extraction", "osmconvert", "csv", "osmfilter", "streetnames" ]
aliases = [ "/questions/76704" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extracted csv only contains 3 streets](/questions/76704/extracted-csv-only-contains-3-streets)

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
<span id="post-76704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76704-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to extract the street name of a city from an osm file (converted from pbf) that I got from geofabrik. I used osmfilter and osmconvert for the extraction, using this command:</p>
<pre><code>osmfilter indonesia-latest.osm --keep=&quot;addr:country= and addr:city=Bandung and addr:street=&quot; --ignore-dependencies --drop-relations --drop-ways |osmconvert64 - --csv=&quot;@oname @id @lon @lat addr:country addr:city addr:street&quot; &gt; street.csv</code></pre>
<p>this is the result:</p>
<pre><code>&quot;node   2756741420  107.6338734 -6.9156038  ID  Bandung Jalan Jenderal Ahmad Yani&quot;
&quot;node   3809732416  107.6065560 -6.9319114  ID  Bandung Jalan Muhammad Toha&quot;
&quot;node   6003232946  107.5775460 -6.9723688  ID  Bandung Jalan Sukamenak&quot;</code></pre>
<p>The problem is, those 3 streets are the only ones extracted in the csv. Is there something wrong with my command or is it the source data? Are there any alternative ways for extraction?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extraction" rel="tag" title="see questions tagged &#39;extraction&#39;">extraction</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '20, 03:21</strong></p>
<img src="https://secure.gravatar.com/avatar/71f61dbbe1a477635bed39e3a11cb8c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceeslt&#39;s gravatar image" />
<p><span>ceeslt</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceeslt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76704" class="comments-container">
<span id="76708"></span>
<div id="comment-76708" class="comment">
<div id="post-76708-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>What data are you hoping to obtain? The OSM information for the street itself? The OSM information for things which have an address on that street? Something else?</p>
</div>
<div id="comment-76708-info" class="comment-info">
<span class="comment-age">(19 Sep '20, 12:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="77003"></span>
<div id="comment-77003" class="comment">
<div id="post-77003-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I was just looking for the names of the street. Sorry I missed your comment all this time.</p>
</div>
<div id="comment-77003-info" class="comment-info">
<span class="comment-age">(08 Oct '20, 10:36)</span> <span class="comment-user userinfo">ceeslt</span>
</div>
</div>
</div>
<div id="comment-tools-76704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76704-form-container" class="comment-form-container">
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

<span id="76706"></span>

<div id="answer-container-76706" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76706-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I know very little about osmosis, but from a data perspective:</p>
<p>You appear to be searching for addresses rather than the names of the streets themselves. In most parts of the world OSM has far better coverage of street names than they do addresses.</p>
<p>Street names are usually recorded as <code>name=*</code> on <a href="https://wiki.openstreetmap.org/wiki/Way">ways</a> representing the street. Streets, tracks and paths all have the same <code>highway</code> key in openstreetmap, see <a href="https://wiki.openstreetmap.org/wiki/Key:highway">this page</a> for a list of values. If your osm file covers more area than you are interested in you will need to get osmosis to only look within that subregion (I can't help with this except to direct you <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.48#Area_Filtering_Tasks">here</a>).</p>
<p>If you actually want the list of streets that have at least one address then you are being a little too restrictive in your query. The <code>addr:country=</code> tag is often omitted entirely as this can usually be inferred from the border. In regions with higher detail the addr:city field can also be left off for the same reason. If you follow this approach you should also look at ways and relations as whole buildings or properties may be tagged with addresses instead of just tagging a POI node within the area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '20, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76706" class="comments-container">
<span id="76913"></span>
<div id="comment-76913" class="comment">
<div id="post-76913-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how do you call the name of the street? I tried</p>
<p>osmfilter indonesia-latest.osm --keep="addr:city=Bandung and addr:street amd name= highway=*" |osmconvert64 - --csv="<a href="https://help.openstreetmap.org/users/260/idoneus">@id</a> <a href="https://help.openstreetmap.org/users/7928/namer-with-roombam">@name</a>" --csv-separator="|" &gt; streetlist.csv</p>
<p>but it doesn't seem to work. (sorry, I'm new with these)</p>
</div>
<div id="comment-76913-info" class="comment-info">
<span class="comment-age">(01 Oct '20, 12:40)</span> <span class="comment-user userinfo">ceeslt</span>
</div>
</div>
<span id="76916"></span>
<div id="comment-76916" class="comment">
<div id="post-76916-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You might benefit from looking at examples of the underlying data and considering whether your query would find them.</p>
<p>Here are the details of a street (or rather a segment of a street) in Bandung: <a href="https://www.openstreetmap.org/way/319194433">https://www.openstreetmap.org/way/319194433</a></p>
<p>If you look at the tags, you can see that it is mapped as highway=primary, and the name is in the "name=" field. There are no addr: tags, which is normal - we would expect addr: tags to apply to buildings and other things located on the street, not the street itself (like this hotel for example: <a href="https://www.openstreetmap.org/way/372063342#map=19/-6.92049/107.60480).">https://www.openstreetmap.org/way/372063342#map=19/-6.92049/107.60480).</a> So if you are looking for highway= objects, you should not have any addr: tags in the query. You would need to restrict the are to Bandung in a different way, but I don't know enough about the tools you are using to say how.</p>
</div>
<div id="comment-76916-info" class="comment-info">
<span class="comment-age">(01 Oct '20, 16:38)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="76955"></span>
<div id="comment-76955" class="comment">
<div id="post-76955-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, now I can understand what I'm looking for data-wise, though since there doesn't seem to be a property that signifies the region(city, province, etc) of the street I'm still looking for ways to filter it.</p>
</div>
<div id="comment-76955-info" class="comment-info">
<span class="comment-age">(05 Oct '20, 04:38)</span> <span class="comment-user userinfo">ceeslt</span>
</div>
</div>
<span id="76998"></span>
<div id="comment-76998" class="comment">
<div id="post-76998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I managed to slice the osm file to contain just the city I'm extracting so there's no need for the addr tag, but I still can't call the name tag. I've tried <a href="https://help.openstreetmap.org/users/7928/namer-with-roombam">@name</a>, name, name=*. and highway:name but still can't get anything.</p>
</div>
<div id="comment-76998-info" class="comment-info">
<span class="comment-age">(08 Oct '20, 02:15)</span> <span class="comment-user userinfo">ceeslt</span>
</div>
</div>
<span id="76999"></span>
<div id="comment-76999" class="comment">
<div id="post-76999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not sure what you mean by "call the name tag". Do your mean you want to filter by name? I am not clear why, as I thought you wanted all names on highway= objects? When you say you can't get anything, do you mean that nothing is written to the csv file, or that the name tag is missing?</p>
</div>
<div id="comment-76999-info" class="comment-info">
<span class="comment-age">(08 Oct '20, 08:05)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="77001"></span>
<div id="comment-77001" class="comment not_top_scorer">
<div id="post-77001-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for my wording, I meant extract the name tag of the streets to write in the csv output, to produce a list of street names. So far the things I've tried have only returned empty results.</p>
</div>
<div id="comment-77001-info" class="comment-info">
<span class="comment-age">(08 Oct '20, 08:29)</span> <span class="comment-user userinfo">ceeslt</span>
</div>
</div>
</div>
<div id="comment-tools-76706" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-76706-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77002"></span>

<div id="answer-container-77002" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77002-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nevermind, I did it using</p>
<p>osmfilter bandung.osm --keep="highway=*" |osmconvert64 - --csv="<a href="https://help.openstreetmap.org/users/260/idoneus">@id</a> name" --csv-separator="|" &gt; jalan.csv</p>
<p>THanks for explaining how osm works!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '20, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/71f61dbbe1a477635bed39e3a11cb8c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceeslt&#39;s gravatar image" />
<p><span>ceeslt</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceeslt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77002" class="comments-container">
&#10;</div>
<div id="comment-tools-77002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77002-form-container" class="comment-form-container">
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

