+++
type = "question"
title = "name= and Wikidata disprepancy"
description = '''How come that the name cannot be set correctly if there is a wikidata link? I find numerous examples with names that cannot be set properly in the map. Almost all have an english language wikidata whereas the correct name is in in some other language. In such cases the english name / wikidata entry ...'''
date = "2021-08-10T19:28:00Z"
lastmod = "2021-08-26T10:04:00Z"
weight = 81258
keywords = [ "wikidata", "name" ]
aliases = [ "/questions/81258" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [name= and Wikidata disprepancy](/questions/81258/name-and-wikidata-disprepancy)

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
<span id="post-81258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81258-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How come that the name cannot be set correctly if there is a wikidata link? I find numerous examples with names that cannot be set properly in the map.</p>
<p>Almost all have an english language wikidata whereas the correct name is in in some other language. In such cases the english name / wikidata entry always take preference.</p>
<p>My examples are for place names in Greenland where the are two officially approved names, an inuit one and a danish. Nevertheless the unofficial english which occur in nwikidata take preference.</p>
<p>Look here: <a href="https://www.openstreetmap.org/#map=11/60.0982/-43.6734">https://www.openstreetmap.org/#map=11/60.0982/-43.6734</a></p>
<ul>
<li>Prince Christian Sound: Real name is Ikerasassuaq</li>
<li>Christian IV Island: Real name is Sammisoq</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wikidata" rel="tag" title="see questions tagged &#39;wikidata&#39;">wikidata</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '21, 19:28</strong></p>
<img src="https://secure.gravatar.com/avatar/210633c3e8ae52ed2bffdb7a36174f64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andershl&#39;s gravatar image" />
<p><span>andershl</span><br />
<span class="score" title="84 reputation points">84</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andershl has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '21, 19:28</strong> </span></p>
</div>
</div>
<div id="comments-container-81258" class="comments-container">
<span id="81461"></span>
<div id="comment-81461" class="comment">
<div id="post-81461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>May be irrelevant: Note that the Wikidata item "name" is a label only, so it's not entirely correct to rely on that as the common name for <code>name=</code> in iD. The names should be properly recorded in properties P2561 (most well-known), P1448 (official), etc.</p>
</div>
<div id="comment-81461-info" class="comment-info">
<span class="comment-age">(25 Aug '21, 05:32)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="81465"></span>
<div id="comment-81465" class="comment">
<div id="post-81465-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess that P2561 and P1448 relate to wikidata. Is that to say I am right in assuming that wrong settings in wikidata will take precedence over corrections in OSM? And if so, how can it be corrected? I have tried in vain and unsuccessfully to edit in wikidata...</p>
</div>
<div id="comment-81465-info" class="comment-info">
<span class="comment-age">(25 Aug '21, 08:03)</span> <span class="comment-user userinfo">andershl</span>
</div>
</div>
<span id="81468"></span>
<div id="comment-81468" class="comment">
<div id="post-81468-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The standard layer in OSM does not refer to wikidata, so corrections to the OSM database will show up there. As mentioned in another comment, updates to low zoom levels may take some time (e.g. a month). But that is nothing to do with wikidata.</p>
</div>
<div id="comment-81468-info" class="comment-info">
<span class="comment-age">(25 Aug '21, 08:30)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="81496"></span>
<div id="comment-81496" class="comment">
<div id="post-81496-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The OSM database containing all the geographical information we (the OSM contributors) collect is completely independent from Wikidata.</p>
<p>Some map creators choose to take information from Wikidata to label their maps. The standard layer on openstreetmap.org does not.</p>
<p>The iD editor locks editing the name if a Wikidata item is present. I don't know the exact rules when it does but in any case there is no linking or copying from Wikidata names to OSM names. And even with the lock in place you can still edit the OSM name as described in this thread and in the tooltip in iD itself.</p>
</div>
<div id="comment-81496-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 09:18)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81499"></span>
<div id="comment-81499" class="comment">
<div id="post-81499-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I realize that is has nothing to do with wikidata, but is simply a matter of (a lot of) patience. So far none of the geographical features that I have corrected for the last 3-4 weeks changed in default OSM.</p>
<p>As to ID: Oh, I found that I can just skip the top part and go to the tags. There I can add, change, and delete anything directly.</p>
<p>Shall just leave wikidata in future chagesets.</p>
<p>Particularly about Greenland: Lots of places have 2-3 inuit names. Until one of them has been selected, the official one will most often be in danish. After assignment the danish will be old. They have a database for it. So far I have seen NO places with english names (strait/bay/glacier). Moreover no iniut names have a danish or english type after their proper name. There are no "XXX Island" or "XXX Ø". The name will be "XXX". old name or name:da may be "YYY" (in danish)whereas name:en may be "XXX Island" all right..</p>
</div>
<div id="comment-81499-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 10:04)</span> <span class="comment-user userinfo">andershl</span>
</div>
</div>
</div>
<div id="comment-tools-81258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81258-form-container" class="comment-form-container">
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

<span id="81261"></span>

<div id="answer-container-81261" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81261-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should be able to edit the name if you scroll down to the Tags area on the left hand side of the screen, which does not enforce the constraint.</p>
<p>Alternatively if wikidata tags are getting in the way of adding correct info to OSM then I would have no compunction in removing them, or renaming them so that the constraint no longer applies. In practice, I don't because I use the work-around above.</p>
<p>In principle tying a name to a wikidata tag aims to promote stability &amp; discourage vandalism. Perhaps more importantly it helps newcomers avoid accidentally renaming significant features. One would hope that people adding wikidata tags do take care to check that the name tag is culturally appropriate when they do so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '21, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-81261" class="comments-container">
<span id="81273"></span>
<div id="comment-81273" class="comment">
<div id="post-81273-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Scrolling down in iD to the tags area is the way to do it. Removing (correct) wikidata link is vandalism in my view.</p>
<p>Just to clarify. This name enforcement is only done in the iD editor. It is not part of the underlying data model.</p>
</div>
<div id="comment-81273-info" class="comment-info">
<span class="comment-age">(11 Aug '21, 10:36)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81275"></span>
<div id="comment-81275" class="comment">
<div id="post-81275-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Any feature which gets in the way of users correcting data is problematic. Wikidata tags aren't great because there are often 2 levels of indirection to check that they are actually correct. If a wikidata tag is assigned to an incorrectly named object, removing the tag if one does not have the time to investigate is hardly vandalism.</p>
</div>
<div id="comment-81275-info" class="comment-info">
<span class="comment-age">(11 Aug '21, 11:52)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="81276"></span>
<div id="comment-81276" class="comment not_top_scorer">
<div id="post-81276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The iD editor is getting in the way of users correcting data, not the wikidata tag. I'm rarely seeing wrong or ambigues wikidata tags. I'd assume most of them are correctly applied. Just removing them because one editor decided to value them more than the name tag is vandalism in my opinion. There is a workaround you described yourself, so why sanction the deletion of the tags?</p>
</div>
<div id="comment-81276-info" class="comment-info">
<span class="comment-age">(11 Aug '21, 12:48)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81277"></span>
<div id="comment-81277" class="comment">
<div id="post-81277-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to throw another point of view, I'm definitely seeing ambiguous wikidata entries. To take a specific example <a href="https://www.wikidata.org/wiki/Q7539634">https://www.wikidata.org/wiki/Q7539634</a> over at wikidata refers to both <a href="https://www.openstreetmap.org/relation/572742">https://www.openstreetmap.org/relation/572742</a> and <a href="https://www.openstreetmap.org/node/34169417">https://www.openstreetmap.org/node/34169417</a> in OSM. OSM just has more detail than wikidata here.</p>
<p>In that example it looks like someone has set "council_name" for what should actually be the "name", perhaps because of this very issue.</p>
</div>
<div id="comment-81277-info" class="comment-info">
<span class="comment-age">(11 Aug '21, 13:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81301"></span>
<div id="comment-81301" class="comment">
<div id="post-81301-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> this is precisely the sort of issue I come across with Wikidata, where wikidata conflates several objects which have rather different semantic meaning on OSM (typically village, political division, administrative division, etc). Many wikidata tags were created from Wikipedia and therefore may reflect notability &amp; merging of articles which reflect wikipedias editorial policies.</p>
</div>
<div id="comment-81301-info" class="comment-info">
<span class="comment-age">(14 Aug '21, 09:22)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="81338"></span>
<div id="comment-81338" class="comment not_top_scorer">
<div id="post-81338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The comments are interesting, but the challenge is still there. For the two example objects no matter what I have tried the english versions still take precedence.</p>
<p>Can anyone make the correct names take precedence and tell how it was done?</p>
<p>And I am fully aware that precendence in displayed map may be dependent upon your nls setting. I am danish, so as for any other object I expect to see the contents of name or name:da.</p>
</div>
<div id="comment-81338-info" class="comment-info">
<span class="comment-age">(17 Aug '21, 09:29)</span> <span class="comment-user userinfo">andershl</span>
</div>
</div>
<span id="81340"></span>
<div id="comment-81340" class="comment not_top_scorer">
<div id="post-81340-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So you have actually been able to update the names in the database as described above. You are now wondering why you don't see the changes in the standard map layer on openstreetmap.org.</p>
<p>The names of these large objects are only displayed on lower zoom levels and map tiles of lower zoom levels are not updated on demand but only infrequently as it takes some time.</p>
<p>So you have to be a bit patient.</p>
</div>
<div id="comment-81340-info" class="comment-info">
<span class="comment-age">(17 Aug '21, 10:04)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81341"></span>
<div id="comment-81341" class="comment">
<div id="post-81341-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As to your last point. The standard map layer on openstreetmap.org uses static names, i.e. it always takes the value from the <code>name</code> key. Other maps may chose to use a different name tags or display names based on the language of the user.</p>
</div>
<div id="comment-81341-info" class="comment-info">
<span class="comment-age">(17 Aug '21, 10:08)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="81349"></span>
<div id="comment-81349" class="comment not_top_scorer">
<div id="post-81349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I could easily change the name tag with ID, but apart from that nothing has happened so far.</p>
<p>So I just need to have a LOT of patience to see it take effect = I should have waited some more weeks. Let's see...</p>
</div>
<div id="comment-81349-info" class="comment-info">
<span class="comment-age">(17 Aug '21, 15:47)</span> <span class="comment-user userinfo">andershl</span>
</div>
</div>
<span id="81446"></span>
<div id="comment-81446" class="comment not_top_scorer">
<div id="post-81446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"A bit patient". What does that incur? Weeks, months or or??</p>
</div>
<div id="comment-81446-info" class="comment-info">
<span class="comment-age">(24 Aug '21, 18:46)</span> <span class="comment-user userinfo">andershl</span>
</div>
</div>
<span id="81448"></span>
<div id="comment-81448" class="comment not_top_scorer">
<div id="post-81448-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For zoom 0-12 it gets updated about once a month to change on the standard layer at osm.org, zoom 13+ should be faster, e.g theroretically in seconds (depending on the caching layers plus rendering queue length).</p>
</div>
<div id="comment-81448-info" class="comment-info">
<span class="comment-age">(24 Aug '21, 19:13)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="81494"></span>
<div id="comment-81494" class="comment not_top_scorer">
<div id="post-81494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I note that some of the cycle maps are faster in reacting (or as I have seen it so far: They DO at least react)....</p>
</div>
<div id="comment-81494-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 07:39)</span> <span class="comment-user userinfo">andershl</span>
</div>
</div>
<span id="81498"></span>
<div id="comment-81498" class="comment not_top_scorer">
<div id="post-81498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you are looking at the maps shown on the main website, CyclOSM updates very frequently. Humanitarian and transit-focused OPNVKarte too.</p>
</div>
<div id="comment-81498-info" class="comment-info">
<span class="comment-age">(26 Aug '21, 10:03)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-81261" class="comment-tools">
<span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-81261-form-container" class="comment-form-container">
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

