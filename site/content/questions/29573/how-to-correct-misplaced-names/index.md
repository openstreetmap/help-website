+++
type = "question"
title = "How to correct misplaced names?"
description = '''Hi. We meet often wrong positioned names. For example, look at all those &quot;island&quot;-s rendered right over water/blue area objects in this link: http://www.openstreetmap.org/#map=13/38.0146/-121.5068 How to correct them?'''
date = "2014-01-03T20:32:00Z"
lastmod = "2014-01-09T15:28:00Z"
weight = 29573
keywords = [ "rendering", "names", "position" ]
aliases = [ "/questions/29573" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to correct misplaced names?](/questions/29573/how-to-correct-misplaced-names)

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
<span id="post-29573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29573-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. We meet often wrong positioned names. For example, look at all those "island"-s rendered right over water/blue area objects in this link:<br />
<a href="http://www.openstreetmap.org/#map=13/38.0146/-121.5068">http://www.openstreetmap.org/#map=13/38.0146/-121.5068</a><br />
How to correct them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-position" rel="tag" title="see questions tagged &#39;position&#39;">position</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jan '14, 20:32</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-29573" class="comments-container">
&#10;</div>
<div id="comment-tools-29573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29573-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="29574"></span>

<div id="answer-container-29574" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29574-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well OSM has a <a href="http://wiki.openstreetmap.org/wiki/Good_practice">basic rule</a> that is called 'don't tag for renderers', so you need to pay attention, that you don't try to tweak just to make it look good at the osm.org default rendering. This might break the semantic of the internal geodata or break other renderings or processing.</p>
<p>So if ther label position is <strong>determind by finding the mean coordinates</strong> of the shape (here: island outer ways), there you can't do anything, as it's calculated by the Mapnik2 renderer. I know that there was a ticket at the old TRAC, but if you like, you can search and maybe open a new <a href="https://github.com/gravitystorm/openstreetmap-carto/issues">issue for the style</a>, that might be pushed upstream to the Mapnik devs.<br />
If the label appears using a <a href="http://wiki.openstreetmap.org/wiki/Key:place">place=* node</a>, you can just move them till it fit's the reality.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '14, 21:49</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-29574" class="comments-container">
<span id="29603"></span>
<div id="comment-29603" class="comment">
<div id="post-29603-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not quite pleased with the answer(s) for the following reasons: 1. The SkippyMap is the OSM's REFERENCE map and it is probably the most visited WEB map of the Planet today; 2. The question implicitly points to a serious systematic error somewhere on the way from the source data until the client rendering; 3. There should be a limit how far the "we are not tagging for renderers" saying should be used as an excuse for serious errors; and 4. The misplaced name examples in the permalink are there in years indicating weaknesses in the public Inspectors used in the data preparation.</p>
</div>
<div id="comment-29603-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 08:55)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
<span id="29604"></span>
<div id="comment-29604" class="comment">
<div id="post-29604-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'm not here to argue, I can just point you to the reasons that I know.</p>
<p>to 1.) There is no 'reference' map as OSM are just data per project definition. An incomplete overview is <a href="http://wiki.openstreetmap.org/wiki/Maps">http://wiki.openstreetmap.org/wiki/Maps</a><br />
to 2.) ? This is Open Source and the bug is/can be reported and be fixed. Currently nobody seems to have the time to do so or an idea for a serious solution without breaking other behaviour/performance.</p>
</div>
<div id="comment-29604-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 09:06)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="29605"></span>
<div id="comment-29605" class="comment">
<div id="post-29605-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>to 3.) It's not an excuse, it's a basic principle to avoid that the community permantly alters the data just because the semantic fit's for ones processing usecase better thant for the others.<br />
to 4.) We don't have inspectors or a professional QA. The <a href="http://wiki.openstreetmap.org/wiki/Quality_Assurance">very basic QA</a> that the (local) community does is basically to monitor the data and guide new users in useful tagging etc.</p>
<p>P.S: I don't like this style of allegations in a public support board. You are welcome to <a href="http://wiki.openstreetmap.org/wiki/Contact">help on working</a> on that topic.</p>
</div>
<div id="comment-29605-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 09:09)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="29607"></span>
<div id="comment-29607" class="comment">
<div id="post-29607-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>iii has given you an accurate answer, sanser. If you are "not quite pleased with it" you are welcome to help fix the underlying issue, but shooting the messenger isn't going to get you anywhere and will make people less likely to help you in future.</p>
</div>
<div id="comment-29607-info" class="comment-info">
<span class="comment-age">(06 Jan '14, 10:09)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-29574" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29574-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29608"></span>

<div id="answer-container-29608" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29608-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Whilst not being a native of that part of the world, I've flown over it a few times. The GNIS imported data (which is the basis for the names there I think) has called some things "islands" and some things "rivers", but from the air it just looks like one large wetland with some "slightly less damp" and some "slightly more damp" areas.<br />
</p>
<p>These "islands" and "rivers" don't always have well-defined boundaries - unfortunately you can't always expect what's there to match your pre-conceived notion of what a feature should look like. Whoever's mapped that area has used GNIS, NHD and (by the looks of it) Bing, and they've done a good job reflecting those sources.<br />
</p>
<p>With regard to the rendering, I can't actually see an example where a label is grossly misplaced, only one where the name being rendered ("Mildred Island", based on GNIS data and matching exactly the imported node) doesn't seem to have an obvious match on Bing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '14, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-29608" class="comments-container">
&#10;</div>
<div id="comment-tools-29608" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29608-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29717"></span>

<div id="answer-container-29717" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29717-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-29717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not answering my own question but targeting the quick and somewhat speculative answers, comments and especially the “vote” column in this forum. Well, I dare to do this even if I know I will get new down/negative votes.<br />
As I understand, the OSM is a professional and scientific public project where arguments talk. So, there is no place there for filings based “like”/”don’t like” type of judgements and where any well-meant and constructive criticism should be welcome. Let me take some bullets:<br />
1. If something is so frequently referenced/used as the SlippyMap (and its layers) by links, extracts and so on, then it is hard to deny that it is a reference map;<br />
2. If someone just a bit carefully looks into the map-extract in the permalink (in the question) he may quickly find at least 10 island names assigned to water objects (rendered over blue background with no islands at all). This fact is so obvious and unquestionable argument in favour of a systematic error assertion that any excuse (like “looking from high above”) is simply speculative. You may “don’t like”-it but never qualified as “not useful” (eventually “don’t understand”);<br />
3. If someone is even more careful, patient and curious he may discover that all the missing islands (holes in water area objects) are actually there. Unfortunately, some of them are inverted to water objects while most of them are overwritten by another water area data layer. And again, this unquestionable systematic error warning I may “don’t like” but never qualified as “not useful”;<br />
4. Finally, this forum is probably the most visited among all OSM lists/forums. Therefore, a warning about a serious systematic error here may trigger the attention of many local editors and renderers. In my opinion, this may be of much larger help than just correcting several errors from the error class.<br />
But still, I may be wrong.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '14, 13:57</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-29717" class="comments-container">
<span id="29719"></span>
<div id="comment-29719" class="comment">
<div id="post-29719-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As far as I can see there is one main problem: Instead of "misplaced names" there are lots of broken or incorrectly/insufficiently tagged multipolygons (according to Bing). They lead to islands being wrongly rendered as water / water wrongly rendered as land. Consequently also the names <em>seem</em> to be incorrectly placed, although they are not. Besides, each name relates from a place=island node. So even if the names would have wrong positions then you could just move the corresponding nodes to the correct position. But here the water/land polygons have to be fixed before doing anything else.</p>
</div>
<div id="comment-29719-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 14:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="29722"></span>
<div id="comment-29722" class="comment">
<div id="post-29722-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@sanser</span> - I don't understand what you're trying to achieve. OSM is a do-ocracy; if something's wrong, go and fix it. Just pointing at something and saying "that's not very good" won't acheive a lot.</p>
</div>
<div id="comment-29722-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 15:12)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="29723"></span>
<div id="comment-29723" class="comment">
<div id="post-29723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>also remember that sometimes things are more complex, so it's hard to evaluate the best solution from afar. for example, Mildred Island is labeled in the middle of the river. if you look at the imagery, you can see what appears to be the outline of an island, but it's now inundated with water. yet, is that still called Mildred Island even though it's more like a reef? and, does the island still appear when the water is under a certain level? if you can find the answers to questions like this, maybe we can help you figure out a better solution.</p>
</div>
<div id="comment-29723-info" class="comment-info">
<span class="comment-age">(09 Jan '14, 15:28)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-29717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29717-form-container" class="comment-form-container">
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

