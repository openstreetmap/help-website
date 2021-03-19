+++
type = "question"
title = "how to add mib files into wireshark"
description = '''Hi All, I understood that it&#x27;s possible to add SNMP MIB files into the Wireshark. The question is:    How could I add the MIB file there?    Eventually, when it&#x27;s added, should I expect to read / write values from the device, like other SNMP applications, like MG-SOFT? Or it&#x27;s merely here to help re...'''
date = "2017-08-02T01:19:00Z"
lastmod = "2017-08-02T07:05:00Z"
weight = 63327
keywords = [ "mib", "snmp" ]
aliases = [ "/questions/63327" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to add mib files into wireshark](/questions/63327/how-to-add-mib-files-into-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63327-score" class="post-score" title="current number of votes">0</div><span id="post-63327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I understood that it's possible to add SNMP MIB files into the Wireshark. The question is:</p><ul><li><p>How could I add the MIB file there?</p></li><li><p>Eventually, when it's added, should I expect to read / write values from the device, like other SNMP applications, like MG-SOFT? Or it's merely here to help reading the capture traffic meaning instead of seeing OIDs in the capture file, I would see object names.</p></li></ul><p>Kind regards, Nima</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mib" rel="tag" title="see questions tagged &#39;mib&#39;">mib</span> <span class="post-tag tag-link-snmp" rel="tag" title="see questions tagged &#39;snmp&#39;">snmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '17, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/c8d537017e8cfda208ea264da153753f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nima&#39;s gravatar image" /><p><span>Nima</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nima has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Aug '17, 01:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-63327" class="comments-container"><span id="63328"></span><div id="comment-63328" class="comment"><div id="post-63328-score" class="comment-score"></div><div class="comment-text"><p>Not a complete answer but may make the answer for the first part not important for you. Wireshark is a read only tool, i.e. it doesn't generate any traffic at all. So you'll only see SNMP messages which were sent by other sources (other machines and other applications running on the same machine where the capture was taken), and having the right MIB loaded only allows Wireshark to translate OIDs into human-readable form as you expect.</p></div><div id="comment-63328-info" class="comment-info"><span class="comment-age">(02 Aug '17, 01:37)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-63327" class="comment-tools"></div><div class="clear"></div><div id="comment-63327-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63337"></span>

<div id="answer-container-63337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63337-score" class="post-score" title="current number of votes">1</div><span id="post-63337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>SNMP MIB configuration can be found in the Preferences, under Name Resolution.</p><p>First use SMI Paths to setup the list of paths where to look for the MIB files.</p><p>Second use SMI Modules to define the MIB modules (that is the module names found in the MIB files) to be loaded.</p><p>Once that is done mark the checkbox Enable OID resolution.</p><p>You will be asked to restart Wireshark, which is needed to actually load the modules from the MIB files.</p><p>The library used to resolve OIDs to names from the modules is rather picky on MIB module correctness. If there are bugs in the MIB modules it will complain loudly. You may mark the checkbox Suppress SMI errors, but it still may not work. Also make sure MIB modules where object and syntaxes are imported from can be loaded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '17, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Aug '17, 04:42</strong> </span></p></div></div><div id="comments-container-63337" class="comments-container"><span id="63339"></span><div id="comment-63339" class="comment"><div id="post-63339-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. I also found out that apparently, it's very important for Wireshark that mib file name must be the same as module name which is described inside that mib file. it directly means that you cannot use a shared mib file for several devices.</p></div><div id="comment-63339-info" class="comment-info"><span class="comment-age">(02 Aug '17, 06:34)</span> <span class="comment-user userinfo">Nima</span></div></div><span id="63340"></span><div id="comment-63340" class="comment"><div id="post-63340-score" class="comment-score"></div><div class="comment-text"><p>Ah yes, another peculiarity of libsmi, the library doing the real work for Wireshark. I don't understand your next comment though: '...it directly means that you cannot use a shared mib file for several devices.' If you want to have a MIB module specific per device type and the various device types have common objects, then collect these in a separate MIB and import them in your device type specific MIBs.</p></div><div id="comment-63340-info" class="comment-info"><span class="comment-age">(02 Aug '17, 07:05)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-63337" class="comment-tools"></div><div class="clear"></div><div id="comment-63337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

