+++
type = "question"
title = "Nominatim problem postcode not returned"
description = '''The request:  http://nominatim.openstreetmap.org/reverse?format=xml&amp;amp;lat=45.41660&amp;amp;lon=5.33245&amp;amp;addressdetails=1 return for the addressparts: &amp;lt;addressparts&amp;gt;  &amp;lt;road&amp;gt;Route de Lyon&amp;lt;/road&amp;gt;  &amp;lt;city&amp;gt;Mottier&amp;lt;/city&amp;gt;  &amp;lt;county&amp;gt;Vienne&amp;lt;/county&amp;gt;  &amp;lt;state&amp;gt;Rhô...'''
date = "2013-02-04T21:19:00Z"
lastmod = "2013-02-04T21:19:00Z"
weight = 19581
keywords = [ "howto", "postcode", "get" ]
aliases = [ "/questions/19581" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim problem postcode not returned](/questions/19581/nominatim-problem-postcode-not-returned)

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
<span id="post-19581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19581-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The request:<br />
<a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=45.41660&amp;lon=5.33245&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=45.41660&amp;lon=5.33245&amp;addressdetails=1</a><br />
<br />
return for the addressparts:<br />
&lt;addressparts&gt;<br />
&lt;road&gt;Route de Lyon&lt;/road&gt;<br />
&lt;city&gt;Mottier&lt;/city&gt;<br />
&lt;county&gt;Vienne&lt;/county&gt;<br />
&lt;state&gt;Rhône-Alpes&lt;/state&gt;<br />
&lt;country&gt;France&lt;/country&gt;<br />
&lt;country_code&gt;fr&lt;/country_code&gt;<br />
&lt;/addressparts&gt;<br />
</p>
<p>But the tag &lt;postcode&gt; is not return</p>
<p>while the postal_code seems to be correctly set for the place Mottier<br />
&lt;node id="34055235" version="5" changeset="7048448" lat="45.4197" lon="5.31648" user="philippekerla" uid="79386" visible="true" timestamp="2011-01-22T10:45:43Z"&gt;<br />
&lt;tag k="code_departement" v="38"/&gt;<br />
&lt;tag k="is_in" v="Europe,France,Isère"/&gt;<br />
&lt;tag k="name" v="Mottier"/&gt;<br />
&lt;tag k="place" v="village"/&gt;<br />
&lt;tag k="population" v="500"/&gt;<br />
&lt;tag k="postal_code" v="38260"/&gt;<br />
&lt;tag k="ref:INSEE" v="38267"/&gt;<br />
&lt;tag k="ref:SIREN" v="213802671"/&gt;<br />
&lt;/node&gt;<br />
</p>
<p>Why ?<br />
Regards Michel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-howto" rel="tag" title="see questions tagged &#39;howto&#39;">howto</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Feb '13, 21:19</strong></p>
<img src="https://secure.gravatar.com/avatar/7c0dfb4787be9ac82896240f6119033e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michel60&#39;s gravatar image" />
<p><span>michel60</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michel60 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-19581" class="comments-container">
&#10;</div>
<div id="comment-tools-19581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19581-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

