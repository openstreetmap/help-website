+++
type = "question"
title = "Overpass ql: Return all parks with playgrounds within polygon"
description = '''Hi  Using overpass Turbo I&#x27;d like to find all parks in the current display that have leisure=playground mapped as polygons or POIs within the polygon of the park. I&#x27;m sorry I have no code worthy of posting, but I assume I would need to first. pass the parks to a variable &amp;amp; then somehow iterate t...'''
date = "2016-01-17T14:58:00Z"
lastmod = "2016-01-22T08:53:00Z"
weight = 47548
keywords = [ "overpass-turbo", "polygon", "overpass-ql" ]
aliases = [ "/questions/47548" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass ql: Return all parks with playgrounds within polygon](/questions/47548/overpass-ql-return-all-parks-with-playgrounds-within-polygon)

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
<span id="post-47548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47548-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>Using overpass Turbo I'd like to find all parks in the current display that have <code>leisure=playground</code> mapped as polygons or POIs within the polygon of the park. I'm sorry I have no code worthy of posting, but I assume I would need to first. pass the parks to a variable &amp; then somehow iterate through them to find if the playgrounds are within.</p>
<p>Would <code>foreach</code> need to be used or is there a simpler method?</p>
<p>I'm not expecting a fully form query, but any pointers in the right directions would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '16, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '16, 19:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47548" class="comments-container">
&#10;</div>
<div id="comment-tools-47548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47548-form-container" class="comment-form-container">
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

<span id="47559"></span>

<div id="answer-container-47559" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47559-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-47559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DaveF has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Right, this will not work with arbitrary polygons as of today, or to be more precise, there has to be a matching area created beforehand on the server, subject to specific area creation rules. Those rules usually require a name tag to be present on the respective polygon. If that's case you can use the following official approach:</p>
<p>overpass turbo link: <a href="http://overpass-turbo.eu/s/dQi">http://overpass-turbo.eu/s/dQi</a></p>
<p>In cases, where no matching area exists, there's the following option, currently available as a preview version:</p>
<p>overpass turbo link: <a href="http://overpass-turbo.eu/s/dOt">http://overpass-turbo.eu/s/dOt</a></p>
<p>This query will return those leisure=playground ways/nodes, which are inside a leisure=park way. Please give it a try. It may be a bit slow, as the dev box runs on somewhat slow hard disks and not SSDs as on production.</p>
<p>Please note that this feature is not available on the official instance on overpass-api.de. Furthermore, it currently has some rough edges and still needs to be reviewed by Roland. Hopefully, we will see this fully functional on overpass-api.de some time in 2016... Stay tuned.</p>
<p>Want to find out more? Take a look at the Github page for lots of further examples and screenshots: <a href="https://github.com/drolbr/Overpass-API/issues/77">https://github.com/drolbr/Overpass-API/issues/77</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '16, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jan '16, 15:45</strong> </span></p>
</div>
</div>
<div id="comments-container-47559" class="comments-container">
<span id="47592"></span>
<div id="comment-47592" class="comment">
<div id="post-47592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Many thanks for your replies. They are close to what I desire except I'd like the parks to be returned not the playgrounds. Is this possible with a small tweak?</p>
</div>
<div id="comment-47592-info" class="comment-info">
<span class="comment-age">(19 Jan '16, 15:13)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="47594"></span>
<div id="comment-47594" class="comment">
<div id="post-47594-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I revised my answer to return the parks instead (this works only in case they have a name=* tag).</p>
<p>If that answers your question, would you mind accepting it? Thanks.</p>
</div>
<div id="comment-47594-info" class="comment-info">
<span class="comment-age">(19 Jan '16, 15:44)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47608"></span>
<div id="comment-47608" class="comment">
<div id="post-47608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you - Accepted. Lots for me to learn. I've never heard of map_to_area or pivot.</p>
</div>
<div id="comment-47608-info" class="comment-info">
<span class="comment-age">(20 Jan '16, 12:02)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="47624"></span>
<div id="comment-47624" class="comment">
<div id="post-47624-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. I used <code>map_to_area</code> as a workaround to get only areas in a certain bounding box. <code>map_to_area</code> will simply add 2400000000 to the way's id. So if you query for a way, then call map_to_area, you'll end up with the respective area (assuming it exists in the first place).</p>
</div>
<div id="comment-47624-info" class="comment-info">
<span class="comment-age">(22 Jan '16, 08:53)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-47559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47559-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47549"></span>

<div id="answer-container-47549" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47549-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's a query that finds playgrounds that are merely nearby the boundaries of parks: <a href="http://overpass-turbo.eu/s/dNx">http://overpass-turbo.eu/s/dNx</a></p>
<p>Not perfect, but probably sufficient for many uses.</p>
<p>I'm not aware that there is a way to check inside of arbitrary geometries. The 'is_in' operator deals with areas, but only a subset of OSM areas are available, parks are not one of them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jan '16, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '16, 15:37</strong> </span></p>
</div>
</div>
<div id="comments-container-47549" class="comments-container">
&#10;</div>
<div id="comment-tools-47549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47549-form-container" class="comment-form-container">
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

