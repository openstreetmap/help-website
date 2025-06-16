+++
type = "question"
title = "[closed] Suspect records found in osm Australia extract."
description = '''Hi there all, while becoming familiar ( and generally playing around with Postgresql + osm data ) with the mapping data system I discovered a set of records, contained within the australia.osm.pbf extract, which might be considered suspect...? I&#x27;ll let higher authorities pass final judgement, howeve...'''
date = "2013-02-07T07:28:00Z"
lastmod = "2013-02-08T01:58:00Z"
weight = 19652
keywords = [ "suspect", "data", "copyright" ]
aliases = [ "/questions/19652" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Suspect records found in osm Australia extract.](/questions/19652/suspect-records-found-in-osm-australia-extract)

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
<span id="post-19652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19652-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-19652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there all,</p>
<p>while becoming familiar ( and generally playing around with Postgresql + osm data ) with the mapping data system I discovered a set of records, contained within the australia.osm.pbf extract, which might be considered suspect...? I'll let higher authorities pass final judgement, however I include the following SQL style report on what I found.</p>
<code> </code>
<hr />
<p>-- QUERY: ~/Development/sql/suspect_tag_report.sql --</p>
<hr />
<p>-- AUTHOR: MjF - 7 Feb 2013 -- -- HOST SYSTEM: SuSE Linux 12.1, postgresl 9.1, PostGIS 2.0 -- -- DB EXTENSIONS: hstore, plpsql, postgis, postgis_topology -- -- OSM DATA: osmosis &lt;== regional data file 'australia.osm.pbf' -- -- OSM SOURCE: GeoFabrik - 1/2/2013 --</p>
<hr />
<p>SELECT tags-&gt;'ref' AS tag_ref, tags-&gt;'name' AS tag_name, tags-&gt;'note' AS tag_note, tags-&gt;'power' AS tag_power, tags-&gt;'source' AS tag_source, tags-&gt;'addr:street' AS tag_addr_street, tags-&gt;'addr:suburb' AS tag_addr_suburb, tags-&gt;'attribution' AS tag_attribution, tags-&gt;'wp:location' AS tag_wp_location, tags-&gt;'wp:location_name' AS tag_wp_location_name FROM public.nodes WHERE tags-&gt;'source' = 'Western Power';</p>
<hr />
<p>-- Above query returns 371 rows with similar output to that which is -- described below.</p>
<hr />
</code>
<p><code>-- SAMPLE OUTPUT: single record - fields of concern marked with '</code><em><code>'. -- ---------- -- tags-&gt;'ref' ==&gt; | 605393 | -- ---------- -- tags-&gt;'name' ==&gt; | 605393 | -- </code><strong><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em></strong><code> </code><strong><em><em><code>-- tags-&gt;'note' ==&gt; * This data has been extracted from a</code></em><code> -- * Western Power database and should </code><em><code>-- * not be uploaded to the OSM database.</code></em><code> --</code></em></strong><code> </code><strong><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em></strong></em><code> -- tags-&gt;'power' ==&gt; | pole | -- ----------------- -- tags-&gt;'source' ==&gt; | Western Power | -- ----------------- -- tags-&gt;'addr:street' ==&gt; | Absolon St | -- -------------- -- tags-&gt;'addr:suburb' ==&gt; | Bumbleyung | -- </code><strong><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em></strong><code> </code><em><code>-- tags-&gt;'attribution' ==&gt; * Permission NOT granted for reuse</code></em><code> -- </code><strong><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em><em><code>*</code></em></strong><code>* -- tags-&gt;'wp:location' ==&gt; | 1 E Dawson St | -- ----------------- -- tags-&gt;'wp:location_name' ==&gt; | 605393 | -- ---------- -- ---------------------&lt; END OF SAMPLE OUTPUT&gt;---------------------- </code></p>
<p>I <em>wonder</em> if someone could take a look at this as it seems rather suspect on first viewing, <strong><em>comments? Suggestions?</em></strong></p>
<p>Regards, Michael.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-suspect" rel="tag" title="see questions tagged &#39;suspect&#39;">suspect</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-copyright" rel="tag" title="see questions tagged &#39;copyright&#39;">copyright</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '13, 07:28</strong></p>
<img src="https://secure.gravatar.com/avatar/bce53667f3f07f337791a358ed85a290?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MJFalconer&#39;s gravatar image" />
<p><span>MJFalconer</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MJFalconer has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>13 Jan '15, 01:35</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-19652" class="comments-container">
<span id="19655"></span>
<div id="comment-19655" class="comment">
<div id="post-19655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmmm...i think things are not that easy at they seem. In Australia's case, the Western Power can be Russia, but this is a Eastern Power. Extrapolating that, America is The Eastern Power in this case but America is a Western Power. So all this raise a question: Why can't we just......get along....^-^</p>
</div>
<div id="comment-19655-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 08:27)</span> <span class="comment-user userinfo">Kaigara</span>
</div>
</div>
<span id="19662"></span>
<div id="comment-19662" class="comment">
<div id="post-19662-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The above example is this node: <a href="https://www.openstreetmap.org/browse/node/1959963292">https://www.openstreetmap.org/browse/node/1959963292</a> if that helps the DWG at all.</p>
</div>
<div id="comment-19662-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 08:58)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="19675"></span>
<div id="comment-19675" class="comment">
<div id="post-19675-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Kaigara</span>: "Western Power" is probably the name of a power company.</p>
</div>
<div id="comment-19675-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 12:23)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-19652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19652-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Relevant link has been given. This issue has been resolved by the DWG." by aseerel4c26 13 Jan '15, 01:35

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19731"></span>

<div id="answer-container-19731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19731-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-19731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>Thanks for the report. The relevant nodes have been deleted and redacted.</p>
<p>Paul Norman,<br />
For the Data Working Group</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '13, 01:58</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span> </br></p>
</div>
</div>
<div id="comments-container-19731" class="comments-container">
&#10;</div>
<div id="comment-tools-19731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19731-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19658"></span>

<div id="answer-container-19658" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19658-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-19658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for reporting this. OSM has the Data Working Group <a href="https://wiki.openstreetmap.org/wiki/Data_working_group">https://wiki.openstreetmap.org/wiki/Data_working_group</a> to deal with such issues.</p>
<p>I've sent them a mail with a pointer to this question. So I think you will get an answer in a couple of days here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '13, 08:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-19658" class="comments-container">
&#10;</div>
<div id="comment-tools-19658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19658-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

