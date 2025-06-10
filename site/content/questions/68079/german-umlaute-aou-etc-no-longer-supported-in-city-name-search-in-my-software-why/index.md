+++
type = "question"
title = "German Umlaute (äöü etc.) no longer supported in city name search in my software - why?"
description = '''Hello, we are using the OSM maps in one of our software products in the following way: Users can enter city names into a search field and the city ´s location (if it is in the database) will be displayed on the map. Recently, cities that have German &quot;Umlaute&quot; (letters like öäü and ß) are no longer f...'''
date = "2019-02-21T09:16:00Z"
lastmod = "2020-06-04T16:36:00Z"
weight = 68079
keywords = [ "german", "usage", "umlaute" ]
aliases = [ "/questions/68079" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [German Umlaute (äöü etc.) no longer supported in city name search in my software - why?](/questions/68079/german-umlaute-aou-etc-no-longer-supported-in-city-name-search-in-my-software-why)

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
<span id="post-68079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68079-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>we are using the OSM maps in one of our software products in the following way: Users can enter city names into a search field and the city ´s location (if it is in the database) will be displayed on the map. Recently, cities that have German "Umlaute" (letters like öäü and ß) are no longer found. This used to work previously, but now it does not. Also, the OSM demo application (OSMCtrlApp.exe) does no longer find cities with the mentioned letters included. Does anybody have an idea why this happens, i.e, what we might have to change in our application?</p>
<p>Thanks</p>
<p>Frank</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-german" rel="tag" title="see questions tagged &#39;german&#39;">german</span> <span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-umlaute" rel="tag" title="see questions tagged &#39;umlaute&#39;">umlaute</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '19, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/b37e0d5cd5e64de536ba6f4368e5bbaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FrankDue&#39;s gravatar image" />
<p><span>FrankDue</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FrankDue has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Feb '19, 06:11</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-68079" class="comments-container">
<span id="68080"></span>
<div id="comment-68080" class="comment">
<div id="post-68080-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You really need to indicate which software you are using.</p>
<p>In particular outside of the core software used to run the OSM website and associated services (that is the rails-port, osm2pgsql, mapnik, nominatim), you should really be asking your supplier.</p>
</div>
<div id="comment-68080-info" class="comment-info">
<span class="comment-age">(21 Feb '19, 09:22)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="68081"></span>
<div id="comment-68081" class="comment">
<div id="post-68081-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Simon,</p>
<p>thanks for your quick feedback.</p>
<p>The program is "Stammbaum 8" and "Stammbaum 9". I am product manager of this program (not a user), but unfortunately I do not find any relating info on the help pages so far with reference to "German Umlaute" subject. Is there a "special" help section somewhere for developers I should address? Thanks again Frank</p>
</div>
<div id="comment-68081-info" class="comment-info">
<span class="comment-age">(21 Feb '19, 09:29)</span> <span class="comment-user userinfo">FrankDue</span>
</div>
</div>
<span id="68084"></span>
<div id="comment-68084" class="comment">
<div id="post-68084-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If <em>you</em> are the product manager and <em>your</em> software fails to find names with umlauts then this is clearly a problem at <em>your</em> side. OSM is just a database. There are no limitations regarding names, any character is supported.</p>
</div>
<div id="comment-68084-info" class="comment-info">
<span class="comment-age">(21 Feb '19, 09:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68085"></span>
<div id="comment-68085" class="comment">
<div id="post-68085-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It might be a coincidence, but there's an OSMCtrlApp.exe <a href="https://github.com/fatelancer/IEC104PowerFlow">here</a>. Does that look familiar (or is it perhaps based on a common ancestor)?</p>
</div>
<div id="comment-68085-info" class="comment-info">
<span class="comment-age">(21 Feb '19, 10:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="68087"></span>
<div id="comment-68087" class="comment">
<div id="post-68087-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And the problem doesn't seem to be OSM website related, as <a href="http://www.openstreetmap.org/search?query=München">http://www.openstreetmap.org/search?query=München</a> seems to work as I'd expect.</p>
</div>
<div id="comment-68087-info" class="comment-info">
<span class="comment-age">(21 Feb '19, 11:36)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="68108"></span>
<div id="comment-68108" class="comment not_top_scorer">
<div id="post-68108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16310/frankdue">@FrankDue</a> you need to tell us which interface and library to OSM you are using in your program. I guess you do not process OSM raw data.</p>
</div>
<div id="comment-68108-info" class="comment-info">
<span class="comment-age">(22 Feb '19, 05:56)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="75141"></span>
<div id="comment-75141" class="comment not_top_scorer">
<div id="post-75141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi there,</p>
<p>Please allow me to resume the talk on German Umlaute problem from last year:</p>
<ol>
<li>The current "OSMCtrlApp.exe" (v1.0.33.0, copyright including 2020) that has been mentioned by SomeoneElse does not find results for example for "München" or "Nürnberg" either. You have to enter "Munchen" or "Nurnberg", in that case the program finds the right results, including "München" and "Nürnberg"</li>
<li><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> We have used the code example from OSM, used and still use the Interface COSMCtrl, Version 1.20 and added our own dialogue. Is tehre maybe a newer version of the interface available? We do not use OSM raw data processing, but the Interface used to work fine when we launched our program, i.e. it found locations if you enter them including Umlaute</li>
</ol>
<p>Maybe we missed something, so I would be happy to get hints how to solve the problem.</p>
<p>Thanks Frank</p>
</div>
<div id="comment-75141-info" class="comment-info">
<span class="comment-age">(04 Jun '20, 13:09)</span> <span class="comment-user userinfo">FrankDue</span>
</div>
</div>
<span id="75142"></span>
<div id="comment-75142" class="comment not_top_scorer">
<div id="post-75142-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is nothing we can do about this. There is no fundamental problem with OpenStreetMap and special characters as already explained before, see for example <a href="https://nominatim.openstreetmap.org/search.php?q=M%C3%BCnchen.">https://nominatim.openstreetmap.org/search.php?q=M%C3%BCnchen.</a> Contact the developers of this software, it sounds like a problem with proper UTF-8 support and/or URL encoding. Alternatively provide a minimal code example to reproduce this problem.</p>
</div>
<div id="comment-75142-info" class="comment-info">
<span class="comment-age">(04 Jun '20, 13:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="75146"></span>
<div id="comment-75146" class="comment not_top_scorer">
<div id="post-75146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Seems to be from <a href="http://www.naughter.com/osmctrl.html">Naughter Software</a>. Please contact them to address the issue.</p>
</div>
<div id="comment-75146-info" class="comment-info">
<span class="comment-age">(04 Jun '20, 16:36)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-68079" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-68079-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

