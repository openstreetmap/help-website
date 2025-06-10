+++
type = "question"
title = "Problem with my JOSM custom presets"
description = '''I have a strange problem with several of my custom presets that I&#x27;ve tried to fix many times without success. Below is my XML preset for tagging certain waterway features. When I invoke it on a new untagged river or stream way, the section to tag source:name (a multiselect key) is always grayed out....'''
date = "2016-11-11T01:10:00Z"
lastmod = "2016-11-12T12:08:00Z"
weight = 52889
keywords = [ "xml", "josm", "presets" ]
aliases = [ "/questions/52889" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with my JOSM custom presets](/questions/52889/problem-with-my-josm-custom-presets)

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
<span id="post-52889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52889-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a strange problem with several of my custom presets that I've tried to fix many times without success. Below is my XML preset for tagging certain waterway features. When I invoke it on a new untagged river or stream way, the section to tag source:name (a multiselect key) is always grayed out. However, if the way is already tagged with waterway=stream or waterway=river, that section behaves as it should and I can select one of the values from the source:name multiselect and apply the tags. Furthermore, the default note "Actual direction of flow unknown." only appears in the first scenario. If there is an existing waterway tag as in the second situation, it does not appear.</p>
<p>The identical behavior is observed in the second item, Lakes/Ponds. If no tags exist on a closedway, the source:name section is grayed out. If a water=pond, or water=lake tag exists before the preset is invoked, everything works as it should.</p>
<p>Can someone lend a hand? Any help or suggestions will be most appreciated.</p>
<p>Dave</p>
<p><strong>(Note: I have replaced &lt; and &gt; with @ symbols to allow XML code to display herein. Also, all "_" get automatically removed when posting XML code)</strong></p>
<pre><code>@presets xmlns=&quot;http://josm.openstreetmap.de/tagging-preset-1.0&quot;@
&#10;@group name=&quot;Waters&quot; @
&#10;@item name=&quot;Waterways&quot; type=&quot;way&quot; icon=&quot;presets/river.png&quot; @
&#10;@combo key=&quot;waterway&quot; text=&quot;Type of waterway&quot; values=&quot;river,stream,canal,drain,ditch&quot; default=&quot;&quot; /@
&#10;@check key=&quot;intermittent&quot; text=&quot;Intermittent?&quot; disable_off=&quot;true&quot; /@
&#10;@text key=&quot;name&quot; text=&quot;Name&quot; default=&quot;&quot;/@
&#10;@text key=&quot;name:th&quot; text=&quot;Name:th&quot; default=&quot;&quot;/@
&#10;@text key=&quot;name:en&quot; text=&quot;Name:en&quot; default=&quot;&quot;/@
&#10;@multiselect key=&quot;source&quot; text=&quot;Source(s)&quot; values=&quot;Bing;survey;Mapbox Satellite;USGS Topo;MSR Topo;GPS;AK GINA&quot; default=&quot;Bing&quot; delete_if_empty=&quot;true&quot;/@
&#10;@space/@
&#10;@multiselect key=&quot;source:name&quot; text=&quot;Source(s) of name&quot; values=&quot;personal_knowledge;survey;USGS Topo;MSR Topo;physical sign on bridge&quot; default=&quot;&quot; delete_if_empty=&quot;true&quot;/@
&#10;@space/@
&#10;@optional@
&#10;@text key=&quot;note&quot; text=&quot;Note&quot; default=&quot;Actual direction of flow unknown.&quot;/@
&#10;@text key=&quot;ref&quot; text=&quot;Reference&quot; default=&quot;&quot;/@
&#10;@text key=&quot;wikipedia:en&quot; text=&quot;Wikipedia&quot; default=&quot;&quot;/@
&#10;@/optional@
&#10;@/item@
&#10;@item name=&quot;Lakes/Ponds&quot; icon=&quot;presets/water.png&quot; type=&quot;node,closedway&quot; @
&#10;@key key=&quot;natural&quot; value=&quot;water&quot; /@
&#10;@check key=&quot;salt&quot; text=&quot;Salt Water&quot; disable_off=&quot;true&quot; /@
&#10;@combo key=&quot;water&quot; text=&quot;Pond, Reservoir, Lake&quot; values=&quot;pond,lake,reservoir,oxbow,lagoon&quot; default=&quot;pond&quot; values_searchable=&quot;true&quot; /@
&#10;@text key=&quot;name&quot; text=&quot;Name&quot; default=&quot;&quot;   /@
&#10;@text key=&quot;ele&quot; text=&quot;Elevation&quot; default=&quot;&quot;   /@
&#10;@multiselect key=&quot;source&quot; text=&quot;Source(s)&quot; values=&quot;Bing;Mapbox Satellite;USGS Topo;MSR Topo;GPS;AK GINA&quot; default=&quot;Bing&quot; /@
&#10;@multiselect key=&quot;source:name&quot; text=&quot;Source(s) of name&quot; values=&quot;personal_knowledge;survey;USGS Topo;MSR Topo;physical sign&quot; default=&quot;&quot;  /@
&#10;@text key=&quot;note&quot; text=&quot;Note&quot; default=&quot;&quot;   /@
&#10;@/item@
&#10;@item name=&quot;Riverbank&quot; icon=&quot;presets/water.png&quot; type=&quot;closedway&quot; @
&#10;@key key=&quot;waterway&quot; value=&quot;riverbank&quot; /@
&#10;@multiselect key=&quot;source&quot; text=&quot;Source(s)&quot; values=&quot;Bing;Mapbox;USGS Topo;MSR Topo;GPS;AK GINA&quot; default=&quot;Bing&quot; /@
&#10;@text key=&quot;note&quot; text=&quot;Note&quot; default=&quot;&quot;   /@
&#10;@/item@
&#10;@item name=&quot;Dam&quot; type=&quot;way,node,closedway&quot; @
&#10;@key key=&quot;waterway&quot; value=&quot;dam&quot; /@
&#10;@text key=&quot;name&quot; text=&quot;Name&quot; default=&quot;&quot;   /@
&#10;@text key=&quot;name:th&quot; text=&quot;Name:th&quot; default=&quot;&quot;/@
&#10;@text key=&quot;name:en&quot; text=&quot;Name:en&quot; default=&quot;&quot;/@
&#10;@multiselect key=&quot;source&quot; text=&quot;Source(s)&quot; values=&quot;Bing;survey;Mapbox Satellite;USGS Topo;MSR Topo;GPS;AK GINA&quot; default=&quot;Bing&quot; delete_if_empty=&quot;true&quot;/@
&#10;@multiselect key=&quot;source:name&quot; text=&quot;Source(s) of name&quot; values=&quot;personal_knowledge;survey;USGS Topo;MSR Topo;physical sign&quot; default=&quot;&quot; delete_if_empty=&quot;true&quot; /@
&#10;@space/@
&#10;@text key=&quot;note&quot; text=&quot;Note&quot; default=&quot;&quot;  /@
&#10;@/item@
&#10;@/group@
&#10;@/presets@</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-presets" rel="tag" title="see questions tagged &#39;presets&#39;">presets</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '16, 01:10</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '16, 09:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-52889" class="comments-container">
&#10;</div>
<div id="comment-tools-52889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52889-form-container" class="comment-form-container">
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

<span id="52895"></span>

<div id="answer-container-52895" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52895-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi <a href="http://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a>,<br />
Looks like the default="" in the multiselect is causing the problem. I removed the default and source:name came up properly. By the way, as per the documentation (<a href="https://josm.openstreetmap.de/wiki/TaggingPresets">https://josm.openstreetmap.de/wiki/TaggingPresets</a>) delete_if_empty attribute is deprecated. The modified entry looks like as follows: <code> &lt;multiselect key="source:name" text="Source(s) of name" values="personal_knowledge;survey;USGS Topo;MSR Topo;physical sign on bridge" /&gt; </code></p>
<p>However, I could not figure out how to get the default value for optional attributes for nodes/ways with pre-existing tags. Could not find anything in the documentation. I would imagine that it is the normal behavior. If the tags are already present, one may not be required to put a default attribute which is optional.</p>
<p>Hope this helps.<br />
Prime</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '16, 07:28</strong></p>
<img src="https://secure.gravatar.com/avatar/94b5bf3dcc698b1a4051d49f3204996e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="primej&#39;s gravatar image" />
<p><span>primej</span><br />
<span class="score" title="106 reputation points">106</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="primej has 2 accepted answers">100%</span> </br></br></p>
</div>
</div>
<div id="comments-container-52895" class="comments-container">
<span id="52896"></span>
<div id="comment-52896" class="comment">
<div id="post-52896-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Many thanks. I tried removing the delete_if_empty parameters first and that seemed to do the trick. I did not know that it had been deprecated. My multiselect and combo statements work as expected now even with the default set to "Bing" or some other value. I also added the values_sort="false" parameter to my combo and multiselect directives because that behaviour, new to JOSM for the past several releases AFAIK, was annoying me.</p>
</div>
<div id="comment-52896-info" class="comment-info">
<span class="comment-age">(12 Nov '16, 12:08)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-52895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52895-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52890"></span>

<div id="answer-container-52890" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52890-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main difference that I see with the preset that I maintain (BENELUX) is that I keep all combo and multiselects in the optional part. I do not notice the behaviour that you see.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '16, 07:01</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-52890" class="comments-container">
<span id="52891"></span>
<div id="comment-52891" class="comment">
<div id="post-52891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks escada - That's not it. I moved those lines into the optional section and they still exhibit the same behavior.</p>
</div>
<div id="comment-52891-info" class="comment-info">
<span class="comment-age">(11 Nov '16, 08:09)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-52890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52890-form-container" class="comment-form-container">
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

