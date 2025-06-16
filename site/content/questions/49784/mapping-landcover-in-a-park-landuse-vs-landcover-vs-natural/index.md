+++
type = "question"
title = "Mapping landcover in a park: landuse vs. landcover vs. natural"
description = '''First some background: I would like to map a park in my city more accurcately. Right now it is only shown as a cemetery on osm.org (tagged both landuse=cemetery and leisure=park), which is somewhat inaccurate. It used to be a cemetery a couple hundred years ago and still has a few headstones, but is...'''
date = "2016-05-22T10:37:00Z"
lastmod = "2016-05-22T12:08:00Z"
weight = 49784
keywords = [ "park", "landcover", "landuse", "natural" ]
aliases = [ "/questions/49784" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Mapping landcover in a park: landuse vs. landcover vs. natural](/questions/49784/mapping-landcover-in-a-park-landuse-vs-landcover-vs-natural)

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
<span id="post-49784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49784-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>First some background: I would like to map a park in my city more accurcately. Right now it is only shown as a cemetery on osm.org (tagged both <code>landuse=cemetery</code> and <code>leisure=park</code>), which is somewhat inaccurate. It used to be a cemetery a couple hundred years ago and still has a few headstones, but is used as a park: going there for a picnic is completely appropriate. I myself like to use osm to get a some idea what a park is like, and that information is not present at the moment.</p>
<p>And then to the question: How should I map the landcover (mostly grass, with a few trees and bushes)? Like my language might hint at, I've understood that the landcover tag is most appropriate. However, looking at a few of the other parks in town, they use <code>landuse=grass</code>. Then there is the <code>natural</code> tag, which I don't really understand much. Is it to be used for areas in natural condition (which parks sometimes contain)? I'm not very comfortable using a new tag, much less changing existing tags, without some guidance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-landcover" rel="tag" title="see questions tagged &#39;landcover&#39;">landcover</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-natural" rel="tag" title="see questions tagged &#39;natural&#39;">natural</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 May '16, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2ff98a0013ee95743984c2fba484816?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valtteri&#39;s gravatar image" />
<p><span>valtteri</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valtteri has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49784" class="comments-container">
&#10;</div>
<div id="comment-tools-49784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49784-form-container" class="comment-form-container">
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

<span id="49787"></span>

<div id="answer-container-49787" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49787-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-49787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="valtteri has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general stick with widely used tags, natural for trees and any patches of wood and bushes (but not for plantings of shrubs). You can also use landuse=grass, but at the very least subtag it in some way (e.g. grass=*). Add paths (whether on grass or not), and other amenities (benches, waste baskets, drinking water etc).</p>
<p>The main problem of using landcover tags is that they represent '''another''' way of tagging things for which there already exist well-established tags which have been in use for over 10 years. This is an example of the problem alluded to here by <a href="https://xkcd.com/927/">XKCD</a></p>
<p>You can change the landuse=cemetery tag to disused:landuse=cemetery, which conveys useful information. I know of at least one cemetery in London which is also a park, a nature reserve and a wood. Although burials no longer take place there, it is emphatically still a cemetery: <a href="https://www.openstreetmap.org/query?lat=52.95697&amp;lon=-1.14118">Abney Park</a>.</p>
<p>This is <a href="https://www.openstreetmap.org/query?lat=52.95697&amp;lon=-1.14118">one example</a> of a park with similar origins. The areas described as meadows are 'no-mow' places which because the park grass has not been fertilised are florally divers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 May '16, 11:35</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-49787" class="comments-container">
<span id="49788"></span>
<div id="comment-49788" class="comment">
<div id="post-49788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you mean by subtagging the grass? I couldn't find any info on the wiki (<a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dgrass).">https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dgrass).</a> I'll ask from others and visit the park again before retagging as disused:landuse=cemetery, but thanks for the suggestion.</p>
</div>
<div id="comment-49788-info" class="comment-info">
<span class="comment-age">(22 May '16, 12:08)</span> <span class="comment-user userinfo">valtteri</span>
</div>
</div>
</div>
<div id="comment-tools-49787" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49787-form-container" class="comment-form-container">
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

