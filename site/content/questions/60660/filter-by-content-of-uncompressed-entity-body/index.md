+++
type = "question"
title = "Filter by content of uncompressed entity body"
description = '''Hi managed to decode the SSL and the readable text is put into uncompressed entity body tab.  I want to only display the packets which contain something in the uncompressed entity body tab if possible?  Here is a little part of a packet for an example to make a filter. cheers. [{&quot;__class__&quot;:&quot;PlayerR...'''
date = "2017-04-07T11:00:00Z"
lastmod = "2017-04-07T11:00:00Z"
weight = 60660
keywords = [ "export-http", "capture-filter", "export-to-csv", "display-filter" ]
aliases = [ "/questions/60660" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter by content of uncompressed entity body](/questions/60660/filter-by-content-of-uncompressed-entity-body)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60660-score" class="post-score" title="current number of votes">0</div><span id="post-60660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi managed to decode the SSL and the readable text is put into uncompressed entity body tab.</p><ol><li>I want to only display the packets which contain something in the uncompressed entity body tab if possible?</li></ol><p>Here is a little part of a packet for an example to make a filter. cheers.</p><pre><code>[{&quot;__class__&quot;:&quot;PlayerRankingVO&quot;,&quot;player&quot;:{&quot;__class__&quot;:&quot;BasePlayerVO&quot;,&quot;player_id&quot;:207633,&quot;name&quot;:&quot;hugandkiss2005&quot;,&quot;avatar&quot;:&quot;portraitIdCrowngirl&quot;},&quot;guildInfo&quot;:{&quot;__class__&quot;:&quot;GuildExtendedInfoVO&quot;,&quot;leaderName&quot;:&quot;henk33&quot;,&quot;id&quot;:4856,&quot;name&quot;:&quot;KEEN&quot;,&quot;banner&quot;:{&quot;__class__&quot;:&quot;GuildBannerVO&quot;,&quot;shapeId&quot;:&quot;guildbanner09&quot;,&quot;shapeColor&quot;:11862016,&quot;symbolId&quot;:&quot;guildicon08&quot;,&quot;symbolColor&quot;:16761643}},&quot;rank&quot;:3249,&quot;points&quot;:35398},

`{&quot;__class__&quot;:&quot;PlayerRankingVO&quot;,&quot;player&quot;:{&quot;__class__&quot;:&quot;BasePlayerVO&quot;,&quot;player_id&quot;:283402,&quot;name&quot;:&quot;SpellChuka&quot;,&quot;avatar&quot;:&quot;portraitIdBlackguy&quot;},&quot;guildInfo&quot;:{&quot;__class__&quot;:&quot;GuildExtendedInfoVO&quot;,&quot;leaderName&quot;:&quot;Princess Lizzie&quot;,&quot;id&quot;:8251,&quot;name&quot;:&quot;\u2665 Lizzie&#39;s Legions! \u2665&quot;,&quot;banner&quot;:{&quot;__class__&quot;:&quot;GuildBannerVO&quot;,&quot;shapeId&quot;:&quot;guildbanner09&quot;,&quot;shapeColor&quot;:11862016,&quot;symbolId&quot;:&quot;guildicon10&quot;,&quot;symbolColor&quot;:16777215}},&quot;rank&quot;:3250,&quot;points&quot;:35391},

{&quot;__class__&quot;:&quot;PlayerRankingVO&quot;,&quot;player&quot;:{&quot;__class__&quot;:&quot;BasePlayerVO&quot;,&quot;player_id&quot;:324222,&quot;name&quot;:&quot;Max1ne&quot;,&quot;avatar&quot;:&quot;portraitAw4F&quot;},&quot;guildInfo&quot;:{&quot;__class__&quot;:&quot;GuildExtendedInfoVO&quot;,&quot;leaderName&quot;:&quot;Thaz&quot;,&quot;id&quot;:5280,&quot;name&quot;:&quot;United Powers&quot;,&quot;banner&quot;:{&quot;__class__&quot;:&quot;GuildBannerVO&quot;,&quot;shapeId&quot;:&quot;guildbanner08&quot;,&quot;shapeColor&quot;:11862016,&quot;symbolId&quot;:&quot;guildicon09&quot;,&quot;symbolColor&quot;:16761643}},&quot;rank&quot;:3251,&quot;points&quot;:35372}</code></pre><p>I've split it up to make it a little easier to read.</p><ol><li>In the end, I'm hoping I can extract these like they are separated now and have then put into an excel spreadsheet or a CSV file, see the example below. I don't know if this is possible within the program itself. If it is can someone point me in the right direction with this too. Or how to export just these packets so I can run a program over them ripping out all the useless crap and formatting it the way I want. Cheers.</li></ol><p>Spreadsheet example: Player ID | NAME | AVATAR | GLD LDR | GLD ID | GLD NAME | RANK | POINTS 207633 | hugsandkiss2005 | portraitIdCrowngirl | henk33 | 4856 | KEEN | 3249 | 35398</p><p>CSV example: 207633, hugsandkiss2005, portraitIdCrowngirl, henk33, 4856, KEEN, 3249, 35398</p><p>Even if all the other info (Banner/symbol id etc) has to be in the spreadsheet or csv. I can work around that.</p><p>Thanks in advance, really appreciate it.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-export-http" rel="tag" title="see questions tagged &#39;export-http&#39;">export-http</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-export-to-csv" rel="tag" title="see questions tagged &#39;export-to-csv&#39;">export-to-csv</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '17, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/10c6535def69c4f7a9a29b2123f86b3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="King0r&#39;s gravatar image" /><p><span>King0r</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="King0r has no accepted answers">0%</span></p></div></div><div id="comments-container-60660" class="comments-container"></div><div id="comment-tools-60660" class="comment-tools"></div><div class="clear"></div><div id="comment-60660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

