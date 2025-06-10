+++
type = "question"
title = "OSM API update a Business listing via API"
description = '''Hello, i&#x27;m trying to update or post business listings via api to the Openstreetmap. However i haven&#x27;t found any information regarding this topic. So my question is: Which APi do i use and post or update to? Where can i find a documentation regarding the data fields. For information on how to transfe...'''
date = "2015-10-27T15:25:00Z"
lastmod = "2015-10-27T22:14:00Z"
weight = 46148
keywords = [ "api", "business", "listing" ]
aliases = [ "/questions/46148" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM API update a Business listing via API](/questions/46148/osm-api-update-a-business-listing-via-api)

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
<span id="post-46148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46148-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i'm trying to update or post business listings via api to the Openstreetmap. However i haven't found any information regarding this topic.</p>
<p>So my question is: Which APi do i use and post or update to? Where can i find a documentation regarding the data fields.</p>
<p>For information on how to transfer the data: For example:</p>
<pre><code>dict = {
name: somename,
street: somestreet,
hours: 1: 12:00-14:00, 2:14:00-16:00
&#10;}</code></pre>
<p>thank you</p>
<p>cheers daniel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-business" rel="tag" title="see questions tagged &#39;business&#39;">business</span> <span class="post-tag tag-link-listing" rel="tag" title="see questions tagged &#39;listing&#39;">listing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '15, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/babcd24432a920316c15e043f3b95bba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dk1990&#39;s gravatar image" />
<p><span>dk1990</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dk1990 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jan '16, 00:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46148" class="comments-container">
&#10;</div>
<div id="comment-tools-46148" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46148-form-container" class="comment-form-container">
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

<span id="46150"></span>

<div id="answer-container-46150" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46150-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-46150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The OSM API described <a href="http://wiki.openstreetmap.org/wiki/API_v0.6">on the Wiki</a> is the one you would use for any attempt at modifying existing OSM data or adding new data. There are also a couple of libraries in various programming languages that make talking to the API easier.</p>
<p>The opening hours syntax in your example is different from what is used in OSM (where day name abbreviations are used).</p>
<p>Please also note that OSM is not primarily a business directory. In the past, people adding business information have made all or some of the following mistakes:</p>
<ul>
<li>adding objects in an automated fashion where data in OSM existed before, leading to duplication.</li>
<li>overwriting valid and surveyed data in OSM with something that came from an "official" data source but was incorrect.</li>
<li>hiding the source of the data - one "online visibility expert" created many OSM accounts in order to hide the fact that he was behind all these edits.</li>
<li>using data sources that are not license-compatible with OSM, for example: company has a list of their branches with addresses but not geo locations, service provider runs the addresses through Google to obtain locations, then adds them to OSM - this is a violation of Google's copyright or terms of use.</li>
<li>building mechanical processes that feed data into OSM but neglecting to read and respond to messages that the community sends in response to these edits, e.g. asking questions or criticising something.</li>
<li>adding "advertising" messages to OSM - see e.g. <a href="https://help.openstreetmap.org/questions/29078/how-to-add-the-tag-paymentbitcoinyes-in-an-openstreetmap-editor-for-the-coinmap">https://help.openstreetmap.org/questions/29078/how-to-add-the-tag-paymentbitcoinyes-in-an-openstreetmap-editor-for-the-coinmap</a> for more.</li>
</ul>
<p>Please do not repeat these mistakes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Oct '15, 15:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Oct '15, 22:15</strong> </span></p>
</div>
</div>
<div id="comments-container-46150" class="comments-container">
<span id="46155"></span>
<div id="comment-46155" class="comment">
<div id="post-46155-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dear Mr Ramm, The Data Updated is done by our business clients (owners of local stores) in combination with our software to make sure no duplicates are added and their correct data is added. We only post real data. I have seen your documentation but there are no field names or anything. I looked for Python 3 packages but couldn't find any documentation regarding this topic.</p>
<p>Would you mind giving me a example for updating and posting new data? (Searching hasn't been a problem) Like this: request.POST(url, data=data) data = {} and one for updating presumably it is done via the osm id? Hours is always difficult with every plattform, so I would appreciate if you would include an example.</p>
<p>We are currently working with Facebook, Foursquare, Factual and Google and would like to add you to our services.</p>
<p>Thanks in advance</p>
<p>Cheers Daniel</p>
</div>
<div id="comment-46155-info" class="comment-info">
<span class="comment-age">(27 Oct '15, 21:52)</span> <span class="comment-user userinfo">dk1990</span>
</div>
</div>
<span id="46156"></span>
<div id="comment-46156" class="comment">
<div id="post-46156-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>A Python API is available <a href="https://github.com/metaodi/osmapi/blob/develop/osmapi/OsmApi.py.">https://github.com/metaodi/osmapi/blob/develop/osmapi/OsmApi.py.</a> During development be sure to use the dev server as described on the API wiki page, not the live server.</p>
<p>You will need to use the NodeCreate/NodeUpdate calls from the Python API, or if you are updating a POI that is recorded in OSM as an area not a point you will need to use WayUpdate. It is imperative to get this right - if you create a new node because you didn't notice that there is already a way that describes the POI then you will create duplicates.</p>
<p>Your clients will have to register an account with OpenStreetMap to make their uploads; you cannot register an account for yourself and let all your clients use that because OSM requests the ability to get in touch with the person who uploads data - which is your clients, not you.</p>
<p>Opening Hours syntax is described <a href="http://wiki.openstreetmap.org/wiki/Key:opening_hours">on the Wiki</a>.</p>
<p>I cannot overstate how important it is to get this right - if you try to dump data into OSM with no regard for the community and its norms then your data will be thrown out, your software blocked and you embarrassed before your clients.</p>
</div>
<div id="comment-46156-info" class="comment-info">
<span class="comment-age">(27 Oct '15, 22:14)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46150-form-container" class="comment-form-container">
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

