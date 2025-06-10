+++
type = "question"
title = "How to Extract Streettype value for Spain addresses"
description = '''Hi Team, OSM is a great boon for lot of developers adding an icing as its free as well. My question here is we are doing address cleansing for some(Spain) data using Google APi(License), for few of the addresses Google Api is not returning StreetType for Spain addresses. is there any way we could ac...'''
date = "2020-04-30T13:32:00Z"
lastmod = "2020-04-30T23:01:00Z"
weight = 74509
keywords = [ "osm" ]
aliases = [ "/questions/74509" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to Extract Streettype value for Spain addresses](/questions/74509/how-to-extract-streettype-value-for-spain-addresses)

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
<span id="post-74509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74509-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Team,</p>
<p>OSM is a great boon for lot of developers adding an icing as its free as well.</p>
<p>My question here is we are doing address cleansing for some(Spain) data using Google APi(License), for few of the addresses Google Api is not returning StreetType for Spain addresses.</p>
<p>is there any way we could acheive finding the streettype for the exception addresses, which google couldnt find using OSM.</p>
<p>ex:- 121 Aldea de Las Cuevas Benidoleig 03759</p>
<p>we dont have any tag for streettype from the API output xml.</p>
<p>Please let me know if you need any additional details.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '20, 13:32</strong></p>
<img src="https://secure.gravatar.com/avatar/fff328c0f1ce62c31405bf2c571009b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bpchintapalli&#39;s gravatar image" />
<p><span>bpchintapalli</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bpchintapalli has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74509" class="comments-container">
<span id="74513"></span>
<div id="comment-74513" class="comment">
<div id="post-74513-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you mean by StreetType? Are you referring to "Calle", "Avenida", and so on? In OpenStreetmap these are generally part of the name, they are not recorded in separate data fields.</p>
<p>What answer would you expect for your example? Looking at the Cadastro <a href="https://www.sedecatastro.gob.es/,">https://www.sedecatastro.gob.es/,</a> as far as I can see Aldea de las Cuevas is an "urbanización" or housing development, and the houses are numbered within the urbanización, with no names for the individual streets. In any case house numbers have not been mapped in OSM for this particular zone (<a href="https://www.openstreetmap.org/#map=17/38.78528/-0.01323)">https://www.openstreetmap.org/#map=17/38.78528/-0.01323)</a> so you wouldn't be able to find individual addresses.</p>
<p>Perhaps the Cadastro would be a more useful source for what you are trying to do? This document mentions a "TipoVia" field (possible values are listed in Annex 1) which might be of interest: <a href="http://www.catastro.meh.es/ws/webservices_catastro.doc">http://www.catastro.meh.es/ws/webservices_catastro.doc</a></p>
</div>
<div id="comment-74513-info" class="comment-info">
<span class="comment-age">(30 Apr '20, 16:42)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="74522"></span>
<div id="comment-74522" class="comment">
<div id="post-74522-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, I meant "Catastro" not "Cadastro".</p>
</div>
<div id="comment-74522-info" class="comment-info">
<span class="comment-age">(30 Apr '20, 23:01)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-74509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74509-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

