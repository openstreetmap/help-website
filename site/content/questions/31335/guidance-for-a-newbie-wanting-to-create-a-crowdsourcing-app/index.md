+++
type = "question"
title = "Guidance for a newbie wanting to create a crowdsourcing app"
description = '''Hi, first day using OSM, first question! The story: I&#x27;m in the middle of 6 weeks of radiotherapy treatment for prostate cancer at Charing Cross Hospital in London. Without going into any detail, the locations of public toilets are quite important for men with prostate issues (as indeed they are for ...'''
date = "2014-03-05T21:36:00Z"
lastmod = "2014-03-09T14:16:00Z"
weight = 31335
keywords = [ "crowdsourcing", "toilet", "amenity" ]
aliases = [ "/questions/31335" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Guidance for a newbie wanting to create a crowdsourcing app](/questions/31335/guidance-for-a-newbie-wanting-to-create-a-crowdsourcing-app)

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
<span id="post-31335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31335-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, first day using OSM, first question!</p>
<p>The story: I'm in the middle of 6 weeks of radiotherapy treatment for prostate cancer at Charing Cross Hospital in London. Without going into any detail, the locations of public toilets are quite important for men with prostate issues (as indeed they are for men and women with all sorts of other health issues)! I am also a web manager used to dealing with open data, apis, mapping and crowdsourcing, although primarily in the cultural sector. So my thoughts immediately turned to whether there was an app available or whether I could build something. In short, anything that already exists appears to be either not working, old and neglected, or covers a specific locality.</p>
<p>So apologies for the fairly long post, but here goes ...</p>
<p>The idea: I'd like to create a simple mobile app (or mobile optimised site) to display the nearest toilets. Initially I'm thinking UK, but there's no reason why it couldn't be more global. I would also like to include a layer of related information that would be useful to people undergoing treatment, primarily contributed by the users themselves (probably stored in either a Wiki or Wordpress type site) and including the sorts of things that wouldn't suit OSM like comments, ratings, tips and advice etc. Much to my surprise (now naive!) there doesn't appear to be an 'official' UK dataset for public conveniences so that's when I thought of OSM. To prove the map concept I have gone to <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> and amended the query to &lt;has-kv k="amenity" v="toilets"/&gt; and it works quite nicely, but I can already see lots of gaps for the area that I know. But lots of potential to get local people with specific knowledge to fill those gaps.</p>
<p>My questions: - is this just reinventing someone else's wheel? - what's the easiest way to pull specific data (in this case based on a query for facility:toilets) statically or dynamically from OSM and display it on a map? I am quite familiar with OpenLayers if that's of any help.<br />
- if my users want to create new facilities I would envisage creating a bespoke interface in my app/site for them and then manually or semi-automatically transferring anything that is appropriate back into OSM. Are there any examples of this sort of indirect crowdsourcing feeding content back into OSM, and are there any issues that would prevent this? - I have long been a fan of Give Me Tap (see link below) and the way they have got private businesses (mainly cafes) to sign up to give free tap water if you present one of their nice shiny bottles. For toilets there is a scheme known as 'Just Can't Wait' but they don't have the same concept of signed-up, approved locations and as such they don't have a map. I'd love to get businesses to sign-up and add themselves, especially those near places like treatment centres. Would displaying these this be something that would fall outside the scope of OSM or could it be embraced within the metadata like access=permissive or access=customers (or even something new like access=onrequest)?</p>
<p>Handy sites: - <a href="http://overpass-turbo.eu/s/2H9">http://overpass-turbo.eu/s/2H9</a> - example of toilet map from OSM</p>
<ul>
<li><p><a href="http://goo.gl/maps/QPK1y">http://goo.gl/maps/QPK1y</a> - same example but using Google maps search</p></li>
<li><p><a href="http://taps.givemetap.co.uk/find_taps">http://taps.givemetap.co.uk/find_taps</a> - initiative to locate sources of free tap water when you present your branded bottle; charitable setup raises funds for drinking water in Africa</p></li>
<li><p><a href="http://www.tripadvisor.co.uk/">http://www.tripadvisor.co.uk/</a> - an obvious example of crowdsourced locations and reviews</p></li>
<li><p><a href="http://www.cyclestreets.net/photomap/">http://www.cyclestreets.net/photomap/</a> - a grassroots crowdsourced map of cycle infrastructure</p></li>
<li><p><a href="http://www.macmillan.org.uk/Cancerinformation/Cancertypes/Prostate/Livingwithprostatecancer/Sideeffects.aspx#DynamicJumpMenuManager_6_Anchor_3">http://www.macmillan.org.uk/Cancerinformation/Cancertypes/Prostate/Livingwithprostatecancer/Sideeffects.aspx#DynamicJumpMenuManager_6_Anchor_3</a> - Just Can't Wait card</p></li>
<li><p><a href="http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dtoilets">http://wiki.openstreetmap.org/wiki/Tag:amenity%3Dtoilets</a> - reference page for toilet nodes</p></li>
</ul>
<p>Any pointers would be gratefully received.</p>
<p>Cheers, James</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crowdsourcing" rel="tag" title="see questions tagged &#39;crowdsourcing&#39;">crowdsourcing</span> <span class="post-tag tag-link-toilet" rel="tag" title="see questions tagged &#39;toilet&#39;">toilet</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '14, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/8578e5fd460f0ed8475e177daf1559ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamesinealing&#39;s gravatar image" />
<p><span>jamesinealing</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamesinealing has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '14, 21:36</strong> </span></p>
</div>
</div>
<div id="comments-container-31335" class="comments-container">
&#10;</div>
<div id="comment-tools-31335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31335-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="31338"></span>

<div id="answer-container-31338" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31338-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-31338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you seen the <a href="http://greatbritishpublictoiletmap.rca.ac.uk/">Great British Public Toilet Map</a>? They may be interested in collaborating.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '14, 22:02</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-31338" class="comments-container">
<span id="31341"></span>
<div id="comment-31341" class="comment">
<div id="post-31341-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Odd, that was one I tried but wasn't really working (I think on my mobile) but it does seem to be now. It's only a London dataset but it certainly seems to be the best I've yet seen, and their roadmap (tewrrible pun, but see 'What's next for the map?' on <a href="http://greatbritishpublictoiletmap.rca.ac.uk/#page-about)">http://greatbritishpublictoiletmap.rca.ac.uk/#page-about)</a> mentions a lot of the issues I've been thinking about, including OSM integration. So many thanks for prompting me to revisit it. I'll get in touch with them.</p>
</div>
<div id="comment-31341-info" class="comment-info">
<span class="comment-age">(05 Mar '14, 22:32)</span> <span class="comment-user userinfo">jamesinealing</span>
</div>
</div>
<span id="31342"></span>
<div id="comment-31342" class="comment">
<div id="post-31342-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know how active it is at the moment as Gail Ramster is a relatively new mum. However, this is certainly the place to start, I don't know of anyone else who has such a comprehensive grasp of both policy issues and sources of data for public toilets (which often turn out to be related to the aforementioned policies).</p>
</div>
<div id="comment-31342-info" class="comment-info">
<span class="comment-age">(05 Mar '14, 22:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="31357"></span>
<div id="comment-31357" class="comment">
<div id="post-31357-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Because several members of OSM have been supporting Gail Ramster's initiatives about providing open data for toilet locations since 2011. It is clear that OSM can provide some of the data and suitable technologies but isnt the whole answer. I find the suggestion that people with prostrate cancer might care whether information about the nearest toilet is provided by an FLOSS data/app or not absurd.</p>
</div>
<div id="comment-31357-info" class="comment-info">
<span class="comment-age">(06 Mar '14, 11:18)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="31375"></span>
<div id="comment-31375" class="comment">
<div id="post-31375-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to say that I've been in touch with Gail who has given a positive response, saying that she is just back working on this. She certainly seems to be the best placed and most knowledgeable person on the subject, so if I can divert what skills and experience I have in her direction that looks to be the best approach.</p>
</div>
<div id="comment-31375-info" class="comment-info">
<span class="comment-age">(06 Mar '14, 22:36)</span> <span class="comment-user userinfo">jamesinealing</span>
</div>
</div>
</div>
<div id="comment-tools-31338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31338-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31356"></span>

<div id="answer-container-31356" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31356-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31356-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31356-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I created <a href="http://toiletmap.org">http://toiletmap.org</a> It was originally a proof of concept to show Gail Ramster (<a href="http://greatbritishpublictoiletmap.rca.ac.uk/)">http://greatbritishpublictoiletmap.rca.ac.uk/)</a> that OpenStreetMap(OSM) had a lot of toilet locations already.</p>
<p>OSM contributors often notice the public toilets while mapping and add the location (can be the difficult bit) but don't add extra attributes you might want to search on (gender, fee, accessibility, opening hours, etc). I intended the website to become a place to search on those attributes and also allow for missing attributes to be added (probably through multiple-user validation before pushing data back to OSM). I also want to include all "away from home toilets" (term used in the business to include cafe toilets etc) and their rules (non-customers can use John Lewis toilets, Tescos it depends on the local store manager, etc). I have some notes(design and code) at home about a phone app version of the site, and this was going to be my next work on it.</p>
<p>There is a lot of interest in this from people like yourself, but there seemed to be no money to keep me able to spend time on it, especially the focus I would have to maintain in order to make a mobile version or app. I even went to the UK Loo of the Year awards, quite a strange experience. It seems commercial interest seemed more directed to supporting the "Changing Places" campaign for disabled toilets the size of a typical shop floor.</p>
<p>As I'm always hacking up new ideas, my attention to ToiletMap.org has gone. I expect the reason it doesn't work is due to a recent web hosting move and I just need to correct the database link. But it will be out of date now anyway. I still snap photos of every toilet I see on holiday and add them to OSM.</p>
<p>You can e-mail me info{at} livingwithdragons[dot]com if you want to speak further, or ask additional questions here and I'll reply later.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '14, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f846f21cfbcf60a35e1f69c2cc74df77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LivingWithDragons&#39;s gravatar image" />
<p><span>LivingWithDr...</span><br />
<span class="score" title="524 reputation points">524</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LivingWithDragons has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-31356" class="comments-container">
<span id="31374"></span>
<div id="comment-31374" class="comment">
<div id="post-31374-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Many thanks, it's great to get the background and start putting pieces together. I've already been in touch with Gail and will drop you a note when I get a minute.</p>
</div>
<div id="comment-31374-info" class="comment-info">
<span class="comment-age">(06 Mar '14, 22:34)</span> <span class="comment-user userinfo">jamesinealing</span>
</div>
</div>
</div>
<div id="comment-tools-31356" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31356-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31413"></span>

<div id="answer-container-31413" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31413-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, it's nice to see new (and old) people interested in this. Thanks for thinking of me!</p>
<p>We have 6 months funding from Nominet to extend our map, which began this month. The aim is to stop focusing just on open data (which is patchy and non-standard) but to crowdsource, and also trawl council sites ourselves. This includes importing and displaying all the OSM toilets. Like toiletmap.org demonstrated, the OSM toilets have lots of locations but not other attributes (like opening hours), whereas council webpages have this information but no efficient way of mapping the locations ("toilet located behind beach huts" is one description I've seen). So we want to match these two data sources, and build on it. All data gathered will be submitted back into OSM.</p>
<p>There are also increasing numbers of community toilets (ones in local businesses that are paid by the council) which can be added, and I like the idea of people adding themselves to a database like Give Me Tap which I've not seen before. Hopefully we'll be able to create an open database that is reliable enough for the public to want to help maintain and improve it. Then others can also make their own toilet-finding apps that meet different user needs.</p>
<p>I'm afraid I can't talk about how we're do this as I haven't a clue - Neontribe do the software side. They seem confident, but we'll also need lots of help!</p>
<p>I'd love to talk more about the OSM data (online or in real life); it'd be great if various projects compliment each other. I'm keen to include as many attributes as is useful (and to make sure we get the right data type for each one), but realistically there's a limit to what people will complete, so we also need to get the right attributes - so on a side note it would be really good to hear what information people with prostate cancer might appreciate.</p>
<p>Does that sound Ok? Please let me know if you think we're going about things the wrong way, as we only want to improve the OSM data and make whatever progress we can towards a decent useable UK database of public and community toilets.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '14, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/7bf2efe0455972906199a53010d8b64c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaillyk&#39;s gravatar image" />
<p><span>gaillyk</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaillyk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '14, 14:15</strong> </span></p>
</div>
</div>
<div id="comments-container-31413" class="comments-container">
&#10;</div>
<div id="comment-tools-31413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31413-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="31414"></span>

<div id="answer-container-31414" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31414-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On a side note, I know Elbatrop's app "Find Toilets" uses OSM data to display facilities and adds any user-generated information back into OSM. So that's another working example to look at, although I haven't looked at it in a couple of years.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '14, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7bf2efe0455972906199a53010d8b64c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gaillyk&#39;s gravatar image" />
<p><span>gaillyk</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gaillyk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31414" class="comments-container">
&#10;</div>
<div id="comment-tools-31414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31414-form-container" class="comment-form-container">
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

