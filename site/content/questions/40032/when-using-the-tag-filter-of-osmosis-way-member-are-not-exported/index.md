+++
type = "question"
title = "When using the tag-filter of osmosis, way member are not exported."
description = '''Hello, I want to export with the following command a certain area with osmosis. In this case, I am interested only certain tags. osmosis.bat --read-pbf file=germany-latest.osm.pbf --bounding-box top=51.2434 left=13.3147 bottom=50.8718 right=14.2280 --tf accept-ways cn_tud:token=* cn_ukd:token=* rout...'''
date = "2015-01-05T10:44:00Z"
lastmod = "2015-01-05T20:41:00Z"
weight = 40032
keywords = [ "osmosis", "accept-ways" ]
aliases = [ "/questions/40032" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [When using the tag-filter of osmosis, way member are not exported.](/questions/40032/when-using-the-tag-filter-of-osmosis-way-member-are-not-exported)

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
<span id="post-40032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40032-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to export with the following command a certain area with osmosis. In this case, I am interested only certain tags.</p>
<pre><code>osmosis.bat --read-pbf file=germany-latest.osm.pbf --bounding-box top=51.2434 left=13.3147 bottom=50.8718 right=14.2280 --tf accept-ways cn_tud:token=* cn_ukd:token=* route=bus,tram,train --used-node --write-xml file=export.osm</code></pre>
<p>The following relation, for example, is exported correctly, because the "tag" "cn_tud: token is included".</p>
<p><code>relation id="7651" version="14" timestamp="2014-10-29T18:50:29Z" changeset="26419250" member type="way" ref="194784029" role="outer" member type="way" ref="23326559" role="inner" member type="way" ref="23326561" role="inner" ... tag k="cn_tud:token" v="SCH" ... relation</code></p>
<p>The "member" of the "type = way" with the "ref = 23326559" is in relation also exists, but the "way" with the "id = 23326559" and the "nodes" is missing.</p>
<p>So the following is missing:</p>
<p><code>way id="23326559" version="4" timestamp="2014-02-08T21:39:57Z" changeset="20455408" nd ref="252592885" ... nd ref="252592885" way</code></p>
<p>What parameters do I need to specify, so that this information can also be exported.</p>
<p>Thank you and best regards</p>
<p>Lakul</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-accept-ways" rel="tag" title="see questions tagged &#39;accept-ways&#39;">accept-ways</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '15, 10:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9b6ed29df9f64447f43439473548aae5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakul83&#39;s gravatar image" />
<p><span>lakul83</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakul83 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '15, 12:15</strong> </span></p>
</div>
</div>
<div id="comments-container-40032" class="comments-container">
<span id="40042"></span>
<div id="comment-40042" class="comment">
<div id="post-40042-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any specific reason why you want to download a full Germany dump for a few hundred ways + relations? Did you already take a look at overpass-turbo.eu instead? Might save you quite a bit of effort.</p>
</div>
<div id="comment-40042-info" class="comment-info">
<span class="comment-age">(05 Jan '15, 20:41)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-40032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40032-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

