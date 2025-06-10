+++
type = "question"
title = "osmfilter tag filter does not filter tags containing colon"
description = '''I genrated and osm file from overpass which consists of some specific tags that i need.  Overpass query way({{bbox}})[&quot;amenity&quot;~&#x27;hospital|clinic|health_post|health_center|nursing_home|dentist&#x27;][&quot;building&quot;][&quot;operator&quot;][&quot;operator:type&quot;][&quot;capacity:beds&quot;];node(w);  I want to filter the file to contain o...'''
date = "2013-08-10T09:40:00Z"
lastmod = "2016-03-24T16:03:00Z"
weight = 25150
keywords = [ "filter", "colon", "osmfilter", "tags" ]
aliases = [ "/questions/25150" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osmfilter tag filter does not filter tags containing colon](/questions/25150/osmfilter-tag-filter-does-not-filter-tags-containing-colon)

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
<span id="post-25150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25150-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I genrated and osm file from overpass which consists of some specific tags that i need.</p>
<p>Overpass query</p>
<pre><code>way({{bbox}})[&quot;amenity&quot;~&#39;hospital|clinic|health_post|health_center|nursing_home|dentist&#39;][&quot;building&quot;][&quot;operator&quot;][&quot;operator:type&quot;][&quot;capacity:beds&quot;];node(w);</code></pre>
<p>I want to filter the file to contain only the above tags. It only outputs the keys without colon in them. i.e i don't get the operator:type and capacity:beds and some others.</p>
<p>Is there a work around for this?</p>
<p>My cmd</p>
<pre><code>osmfilter health_facility.osm --keep-tags=&quot;all amenity= building= operator= operator:type= capacity:beds=&quot; -o=filteres.osm</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-colon" rel="tag" title="see questions tagged &#39;colon&#39;">colon</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '13, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-25150" class="comments-container">
<span id="25210"></span>
<div id="comment-25210" class="comment">
<div id="post-25210-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if you cannot get any help here, try the discussion page of <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">http://wiki.openstreetmap.org/wiki/Osmfilter</a> in the OSM wiki.</p>
</div>
<div id="comment-25210-info" class="comment-info">
<span class="comment-age">(11 Aug '13, 20:08)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="25230"></span>
<div id="comment-25230" class="comment">
<div id="post-25230-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you really sure that there are objects in your input osm file that have the attributes with the colon? Please provide an overpass-turbo permalink, so we can experiment with the data. I have no problems filtering on keys with a colon in them.</p>
</div>
<div id="comment-25230-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 12:07)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="25231"></span>
<div id="comment-25231" class="comment">
<div id="post-25231-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Do you mean the Katmandu area in Nepal? <a href="http://overpass-turbo.eu/s/Ku">http://overpass-turbo.eu/s/Ku</a></p>
</div>
<div id="comment-25231-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 12:35)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="48813"></span>
<div id="comment-48813" class="comment">
<div id="post-48813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Same here, I have an osm with nodes like these.</p>
<pre><code>&lt;way id=&quot;5560559&quot; version=&quot;2&quot; timestamp=&quot;2010-04-02T23:40:53Z&quot; changeset=&quot;4309152&quot; uid=&quot;20587&quot; user=&quot;balrog-kun&quot;&gt;
    &lt;nd ref=&quot;41190944&quot;/&gt;
    &lt;nd ref=&quot;41190945&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;North Jackson Circle&quot;/&gt;
    &lt;tag k=&quot;highway&quot; v=&quot;residential&quot;/&gt;
    &lt;tag k=&quot;tiger:cfcc&quot; v=&quot;A41&quot;/&gt;
    &lt;tag k=&quot;tiger:tlid&quot; v=&quot;128331343&quot;/&gt;
    &lt;tag k=&quot;tiger:county&quot; v=&quot;Maricopa, AZ&quot;/&gt;
    &lt;tag k=&quot;tiger:source&quot; v=&quot;tiger_import_dch_v0.6_20070809&quot;/&gt;
    &lt;tag k=&quot;tiger:reviewed&quot; v=&quot;no&quot;/&gt;
    &lt;tag k=&quot;tiger:zip_left&quot; v=&quot;85205&quot;/&gt;
    &lt;tag k=&quot;tiger:name_base&quot; v=&quot;Jackson&quot;/&gt;
    &lt;tag k=&quot;tiger:name_type&quot; v=&quot;Cir&quot;/&gt;
    &lt;tag k=&quot;tiger:separated&quot; v=&quot;no&quot;/&gt;
    &lt;tag k=&quot;tiger:zip_right&quot; v=&quot;85205&quot;/&gt;
    &lt;tag k=&quot;tiger:name_direction_prefix&quot; v=&quot;N&quot;/&gt;
&lt;/way&gt;</code></pre>
<p>which I want to filter out with this instruction</p>
<pre><code>osmosis --read-xml arizona_highways_residentials.osm --tf accept-ways tiger:county=&quot;Maricopa, AZ&quot; --tf reject-relations --used-node --write-xml arizona_maricopa_highways_residentials.osm</code></pre>
<p>But it does not work, it works if I do highway=residential, though</p>
</div>
<div id="comment-48813-info" class="comment-info">
<span class="comment-age">(24 Mar '16, 09:12)</span> <span class="comment-user userinfo">lanzalibre</span>
</div>
</div>
<span id="48814"></span>
<div id="comment-48814" class="comment">
<div id="post-48814-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/12110/lanzalibre">@lanzalibre</a> is that related to this question in any way? They were using osmfilter; you're using osmosis? I'd suggest asking a separate question (and say what OS you're using, as that can change what you type on the command line before osmosis even sees it).</p>
</div>
<div id="comment-48814-info" class="comment-info">
<span class="comment-age">(24 Mar '16, 09:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48823"></span>
<div id="comment-48823" class="comment not_top_scorer">
<div id="post-48823-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are very right. Here is the corresponding osmfilter query with the exact same result</p>
<p>osmfilter arizona_highways_residentials.osm --keep="tiger:county='Maricopa, AZ'" &gt; arizona_maricopa_highways_residentials.osm</p>
</div>
<div id="comment-48823-info" class="comment-info">
<span class="comment-age">(24 Mar '16, 16:03)</span> <span class="comment-user userinfo">lanzalibre</span>
</div>
</div>
</div>
<div id="comment-tools-25150" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-25150-form-container" class="comment-form-container">
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

<span id="25232"></span>

<div id="answer-container-25232" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25232-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="amritkarma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have performed the following steps:</p>
<ol>
<li>Perform Overpass query from <a href="http://overpass-turbo.eu/s/Ku">http://overpass-turbo.eu/s/Ku</a></li>
<li>Download data (Export tab, then "as raw data from overpass interpreter") as nepal_health.osm</li>
<li><code>osmfilter.exe nepal_health.osm --keep-tags="all amenity= building= operator= operator:type= capacity:beds=" &gt; nepal_health_filtered.osm</code></li>
</ol>
<p>The resulting document contains all the tags you mentioned.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Aug '13, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-25232" class="comments-container">
&#10;</div>
<div id="comment-tools-25232" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25232-form-container" class="comment-form-container">
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

