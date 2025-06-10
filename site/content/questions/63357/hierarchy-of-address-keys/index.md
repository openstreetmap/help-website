+++
type = "question"
title = "Hierarchy of address keys"
description = '''Hi, I need a full hierarchy of all address keys. In https://wiki.openstreetmap.org/wiki/Nominatim#Hierarchy few keys only present in the hierarchy.  EDIT: I need to exactly know the tag or key names associated with each of the subdivision values present here : https://wiki.openstreetmap.org/wiki/Tag...'''
date = "2018-05-07T09:10:00Z"
lastmod = "2018-05-07T13:36:00Z"
weight = 63357
keywords = [ "hierarchy", "osm", "address" ]
aliases = [ "/questions/63357" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Hierarchy of address keys](/questions/63357/hierarchy-of-address-keys)

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
<span id="post-63357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63357-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I need a full hierarchy of all address keys.</p>
<p>In <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Hierarchy">https://wiki.openstreetmap.org/wiki/Nominatim#Hierarchy</a> few keys only present in the hierarchy.</p>
<p><strong>EDIT:</strong> I need to exactly know the tag or key names associated with each of the subdivision values present here : <a href="https://wiki.openstreetmap.org/wiki/Tag:boundary=administrative#10_admin_level_values_for_specific_countries">https://wiki.openstreetmap.org/wiki/Tag:boundary=administrative#10_admin_level_values_for_specific_countries</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hierarchy" rel="tag" title="see questions tagged &#39;hierarchy&#39;">hierarchy</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '18, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 May '18, 13:31</strong> </span></p>
</div>
</div>
<div id="comments-container-63357" class="comments-container">
<span id="63358"></span>
<div id="comment-63358" class="comment">
<div id="post-63358-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you mean you need a reverse geo-coding engine that returns "all" address keys? Or?</p>
<p>Naturally "all" address keys are rarely in use in the real world, so most of the time most of them are going to be empty see <a href="https://wiki.openstreetmap.org/wiki/Key:addr">https://wiki.openstreetmap.org/wiki/Key:addr</a></p>
</div>
<div id="comment-63358-info" class="comment-info">
<span class="comment-age">(07 May '18, 10:24)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="63359"></span>
<div id="comment-63359" class="comment">
<div id="post-63359-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Address formats vary by country. Do you have any country/ies in mind?</p>
</div>
<div id="comment-63359-info" class="comment-info">
<span class="comment-age">(07 May '18, 10:41)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="63361"></span>
<div id="comment-63361" class="comment">
<div id="post-63361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I need the hierarchy of 'all' possible addres keys. For example to below address i hope the hierarchy is countrycode&gt;country&gt;postalcode&gt;state&gt;state_district&gt;hamlet&gt;city_district&gt;suburb&gt;neighbourhood&gt;road</p>
<pre><code>  &quot;road&quot;:&quot;3rd Street&quot;,
  &quot;neighbourhood&quot;:&quot;F Block&quot;,
  &quot;suburb&quot;:&quot;Ward 101&quot;,
  &quot;city_district&quot;:&quot;Zone 8 Anna Nagar&quot;,
  &quot;hamlet&quot;:&quot;Kaveri Rangan Colony&quot;,
  &quot;state_district&quot;:&quot;Chennai district&quot;,
  &quot;state&quot;:&quot;Tamil Nadu&quot;,
  &quot;postcode&quot;:&quot;600102&quot;,
  &quot;country&quot;:&quot;India&quot;,
  &quot;country_code&quot;:&quot;in&quot;</code></pre>
</div>
<div id="comment-63361-info" class="comment-info">
<span class="comment-age">(07 May '18, 13:09)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="63362"></span>
<div id="comment-63362" class="comment">
<div id="post-63362-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/30/rorym"></a><a href="https://help.openstreetmap.org/users/30/rorym">@rorym</a>: I need to create the hierarchy for all countries, is there a generic way possible ? Or is there a meta-admin-level info based on country, i.e the sub-divisions address keys to a country ?</p>
</div>
<div id="comment-63362-info" class="comment-info">
<span class="comment-age">(07 May '18, 13:36)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-63357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63357-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

