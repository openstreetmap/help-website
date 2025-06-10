+++
type = "question"
title = "Power plant not being shown on openstreet map"
description = '''On openinframap.org I can see the Wildorado Wind 1 and 2 farms: https://openinframap.org/#14/35.29193/-102.31629 But on openstreemap.org only the turbines are shown: https://openinframap.org/#14/35.29193/-102.31629 The outline is not being shown (so I can&#x27;t edit it). Secondly the name is not being f...'''
date = "2019-12-27T22:31:00Z"
lastmod = "2019-12-29T09:38:00Z"
weight = 72242
keywords = [ "search", "infrastructure" ]
aliases = [ "/questions/72242" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Power plant not being shown on openstreet map](/questions/72242/power-plant-not-being-shown-on-openstreet-map)

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
<span id="post-72242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72242-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On openinframap.org I can see the Wildorado Wind 1 and 2 farms: <a href="https://openinframap.org/#14/35.29193/-102.31629">https://openinframap.org/#14/35.29193/-102.31629</a></p>
<p>But on openstreemap.org only the turbines are shown: <a href="https://openinframap.org/#14/35.29193/-102.31629">https://openinframap.org/#14/35.29193/-102.31629</a> The outline is not being shown (so I can't edit it). Secondly the name is not being found in the search results:</p>
<p>openinframap.org showing Wildorado Wind 1: <img src="https://help.openstreetmap.org/upfiles/openinframap_showing_name_of_wind_farm.png" alt="openinframap.org showing Wildorado Wind 1" /></p>
<p>openstreemap.org not finding name of wind farm, or showing the name of wind farm or the outline: <img src="https://help.openstreetmap.org/upfiles/openstreemap_not_finding_name_of_wind_farm.png" alt="openstreemap.org not finding name of wind farm" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-infrastructure" rel="tag" title="see questions tagged &#39;infrastructure&#39;">infrastructure</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '19, 22:31</strong></p>
<img src="https://secure.gravatar.com/avatar/688a8eb05930e8c8cd2606aa27ff8888?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TFJamMan&#39;s gravatar image" />
<p><span>TFJamMan</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TFJamMan has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Dec '19, 23:29</strong> </span></p>
</div>
</div>
<div id="comments-container-72242" class="comments-container">
<span id="72244"></span>
<div id="comment-72244" class="comment">
<div id="post-72244-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There are two questions. The first being that it's not found in the search results. I have no answer for that yet.</p>
<p>The second being that its outline is not shown so you can't edit it. The wind farm shown on openinframap.org references a open street map object with a whole list of member nodes: <a href="https://www.openstreetmap.org/relation/6804129#map=14/35.2836/-102.3052">https://www.openstreetmap.org/relation/6804129#map=14/35.2836/-102.3052</a> as opposed to referencing a "way" like for other objects: <a href="https://www.openstreetmap.org/way/174863750#map=19/35.29645/-101.74726">https://www.openstreetmap.org/way/174863750#map=19/35.29645/-101.74726</a> So I think open infrastructure just draws the polygon outline automatically and therefore there's nothing for openstreetmap to render with a label of "Wildorado Wind 1" on it.</p>
</div>
<div id="comment-72244-info" class="comment-info">
<span class="comment-age">(28 Dec '19, 00:13)</span> <span class="comment-user userinfo">TFJamMan</span>
</div>
</div>
<span id="72248"></span>
<div id="comment-72248" class="comment">
<div id="post-72248-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I guess Nominatim does not recognize relations of type=site, hence it does not show up in the search results on osm.org</p>
</div>
<div id="comment-72248-info" class="comment-info">
<span class="comment-age">(28 Dec '19, 07:15)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="72267"></span>
<div id="comment-72267" class="comment">
<div id="post-72267-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>With regard to "its outline is not shown so you can't edit it", I think you're right - OpenInfraMap seems to be inferring the polygon based on the nodes.:</p>
<p>Via OSM's data layer or query button you can get to one of the <a href="https://www.openstreetmap.org/node/944049221">nodes</a>, and from there you can click through to the <a href="https://www.openstreetmap.org/relation/6804129">relation</a>.</p>
</div>
<div id="comment-72267-info" class="comment-info">
<span class="comment-age">(29 Dec '19, 00:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="72271"></span>
<div id="comment-72271" class="comment">
<div id="post-72271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17524/tfjamman">@TFJamMan</a> If you see a need, perhaps you could suggest to add a label node for wind farms.</p>
</div>
<div id="comment-72271-info" class="comment-info">
<span class="comment-age">(29 Dec '19, 09:38)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-72242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72242-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

