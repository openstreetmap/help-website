+++
type = "question"
title = "6 bit ASCII representation"
description = '''Hi, Can I display the raw data in content packet in 6 bit ASCII instead of the 8 bit ASCII which presented as default? Thank you'''
date = "2013-06-30T15:37:00Z"
lastmod = "2016-09-12T16:43:00Z"
weight = 22490
keywords = [ "6bit", "ascii" ]
aliases = [ "/questions/22490" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [6 bit ASCII representation](/questions/22490/6-bit-ascii-representation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Can I display the raw data in content packet in 6 bit ASCII instead of the 8 bit ASCII which presented as default?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">6bit ascii</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '13, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/182ef93b70cfdfc6b73831b8970f01b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="morton&#39;s gravatar image" /><p>morton<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="morton has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '13, 18:13</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-22490" class="comments-container"><span id="22491"></span><div id="comment-22491" class="comment"><div id="post-22491-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "6-bit ASCII" and "raw data"? ASCII is a 7-bit character set; Wireshark <em>should</em>, in the hex/ASCII dump pane, be displaying <em>printable</em> characters that have the 8th bit clear as their ASCII values and <em>should</em> be displaying everything else, whether it's non-printable ASCII or is a byte with the 8th bit set, as a ".".</p></div><div id="comment-22491-info" class="comment-info"><span class="comment-age">(30 Jun '13, 17:01)</span> Guy Harris ♦♦</div></div><span id="22514"></span><div id="comment-22514" class="comment"><div id="post-22514-score" class="comment-score"></div><div class="comment-text"><p>In the Hex/ASCII dump pane the values are presented in 8-bit ASCII format. Apparently in the world there is also 6-BIT ASCII format. Can I configure wireshark to display the data in this pane in this format?</p><p>Thank you</p></div><div id="comment-22514-info" class="comment-info"><span class="comment-age">(01 Jul '13, 08:08)</span> morton</div></div><span id="22532"></span><div id="comment-22532" class="comment"><div id="post-22532-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Apparently in the world there is also 6-BIT ASCII format.</p></blockquote><p>Can you please add an example where 6-bit ASCII is needed (maybe a network protocol supported by Wireshark)?</p></div><div id="comment-22532-info" class="comment-info"><span class="comment-age">(01 Jul '13, 21:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22490" class="comment-tools"></div><div class="clear"></div><div id="comment-22490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="22517"></span>

<div id="answer-container-22517" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22517-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Apparently in the world there is also 6-BIT ASCII format.</p></blockquote><p>Yes, there is, if your part of the world is running ancient versions of various DEC operating systems - where "ancient" means "from the 1960's", not "from the 1980's" or "from the 1990's".</p><p>Nobody's contributed any dissectors for what network protocols they used, if any (DECNET dates back from a time <em>after</em> DEC started using 7-bit ASCII; the <a href="http://h71000.www7.hp.com/wizard/decnet/dap_v5_6_0.txt">DECNET Data Access Protocol</a> doesn't seem to have any support for 6-bit "half-ASCII"), and nobody's contributed any code to support displaying various encodings of 6-bit "half-ASCII" in whatever way it's put into 8-bit bytes, so, no, there's no way to display "half-ASCII" in the hex/ASCII pane in Wireshark.</p><p>The <a href="http://www.ecma-international.org/publications/files/ECMA-ST-WITHDRAWN/ECMA-1,%201st%20Edition,%20March%201963.pdf">ECMA 6-bit character code</a> has a URL with the word "WITHDRAWN" in it, and dates back to 1963, so it's also ancient.</p><p>The only way you'll ever see any support for any such "half-ASCII" encoding in the hex/text pane would be if a specification for the way in which that encoding works with 8-bit bytes were supplied to us <em>and</em> if that encoding mechanism put one 6-bit character into every 8-bit byte; if it tries to, for example, pack 8 6-bit characters into 6 8-bit bytes, that's unlikely ever to be supported.</p><p>If a specification for a protocol using a "half-ASCII" of that type were provided, a dissector for it might be implemented; you wouldn't see that in the hex/text pane, but you would see it in the packet details pane.</p><p>(Note that a 6-bit version of ASCII wouldn't be ASCII; ASCII has 128 code points, and you can't fit that into 6 bits without some escape scheme, as a 6-bit character can only contain one of 64 possible values, 0 to 63.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22517" class="comments-container"></div><div id="comment-tools-22517" class="comment-tools"></div><div class="clear"></div><div id="comment-22517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22515"></span>

<div id="answer-container-22515" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22515-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are <a href="http://en.wikipedia.org/wiki/Six-bit_character_code">6-bit character codes</a>, however, there is (currently) no support for those character representations in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 08:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-22515" class="comments-container"></div><div id="comment-tools-22515" class="comment-tools"></div><div class="clear"></div><div id="comment-22515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22533"></span>

<div id="answer-container-22533" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22533-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>@morton: If you are talking about NMEA AIS messages, then they are indeed '6-bit ASCII' encoded.</p><p>6-bit ASCII explanation and samples</p><blockquote><p><code>http://www.bosunsmate.org/ais/</code><br />
<code>http://www.it-digin.com/blog/?p=20</code><br />
</p></blockquote><p>NMEA information</p><blockquote><p><code>http://en.wikipedia.org/wiki/NMEA_0183</code><br />
<code>http://www.nmea.org/content/nmea_standards/nmea_0183_v_410.asp</code><br />
</p></blockquote><p>However, there is no NMEA support in Wireshark, hence no way to 'translate' the 8-bit ASCII representation to AIS 6-bit ASCII.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '13, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Jul '13, 03:30</p></div></div><div id="comments-container-22533" class="comments-container"><span id="22541"></span><div id="comment-22541" class="comment"><div id="post-22541-score" class="comment-score"></div><div class="comment-text"><p>Well, more like "6-bit <em>subset</em> of ASCII"; you can't fit all of ASCII into 6 bits per character. <a href="http://www.bosunsmate.org/ais/#nmea">Subtract 48</a> doesn't work for control characters or for SP through /, as the result is negative.</p></div><div id="comment-22541-info" class="comment-info"><span class="comment-age">(02 Jul '13, 00:20)</span> Guy Harris ♦♦</div></div><span id="22544"></span><div id="comment-22544" class="comment"><div id="post-22544-score" class="comment-score"></div><div class="comment-text"><p>I know, but 'they' reference 'their' encoding as <strong>6 bit ASCII</strong> (or at least the guys who wrote about it - as I don't have access to the specs I can't verify it. That's why I mentioned it here, just in case...</p></div><div id="comment-22544-info" class="comment-info"><span class="comment-age">(02 Jul '13, 00:33)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22533" class="comment-tools"></div><div class="clear"></div><div id="comment-22533-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55502"></span>

<div id="answer-container-55502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55502-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The spec is here: <a href="https://www.itu.int/rec/R-REC-M.1371/en">https://www.itu.int/rec/R-REC-M.1371/en</a> or ESR created <a href="http://catb.org/gpsd/AIVDM.html">AIVDM.html</a></p><p>My decoder for AIS is here: <a href="https://github.com/schwehr/libais">https://github.com/schwehr/libais</a></p><p>Or GPSD would also be a decent choice for a decoder.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '16, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/573c8dd18fa20d348c3d072962f36020?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schwehr&#39;s gravatar image" /><p>schwehr<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schwehr has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-55502" class="comments-container"></div><div id="comment-tools-55502" class="comment-tools"></div><div class="clear"></div><div id="comment-55502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

