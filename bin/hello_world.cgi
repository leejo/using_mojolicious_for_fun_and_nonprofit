#!/usr/bin/env perl

use strict;
use warnings;
use utf8;

use CGI qw/ -utf8 /;

my $cgi = CGI->new;

binmode( STDOUT,":utf8" );

print $cgi->header(
    -type    => 'text/html',
    -charset => 'utf-8',
);

print "Bonjour à tous depuis CGI.pm";
